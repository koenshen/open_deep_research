#!/usr/bin/env python3
"""Generate Open Deep Research reports for LiveResearchBench."""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import json
import os
import re
import sys
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs" / "liveresearchbench"
BEIJING_TZ = ZoneInfo("Asia/Shanghai")

# LangGraph CLI loads this file through langgraph.json. This standalone runner
# needs to load it explicitly.
load_dotenv(PROJECT_ROOT / ".env")

from open_deep_research.configuration import Configuration  # noqa: E402
from open_deep_research.deep_researcher import deep_researcher_builder  # noqa: E402
from open_deep_research.utils import TavilyUsageLimitExceeded  # noqa: E402
from liveresearchbench_stats import ResearchStatsCallback  # noqa: E402

try:
    from liveresearchbench.common.io_utils import (  # noqa: E402
        load_liveresearchbench_dataset,
    )
except ImportError as exc:  # pragma: no cover - exercised by installation state
    raise SystemExit(
        "LiveResearchBench is not installed in this environment. Run:\n"
        "  uv pip install -e ../LiveResearchBench"
    ) from exc


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Run Open Deep Research on LiveResearchBench questions and save "
            "reports in the benchmark's expected directory layout."
        )
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Base output directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--model-name",
        help=(
            "Name of the output subdirectory/system. Defaults to a name derived "
            "from SEARCH_API and RESEARCH_MODEL."
        ),
    )
    parser.add_argument(
        "--qid",
        action="append",
        help="Run only this query ID. Repeat --qid to select multiple questions.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Run only the first N selected questions (useful for smoke tests).",
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=1,
        help="为了 resume 机制防止原子写错误，所以并发数只能是 1",
    )
    parser.add_argument(
        "--progress-interval",
        type=float,
        default=30.0,
        help=(
            "Seconds between in-progress status messages; use 0 to disable "
            "heartbeats (default: 30)."
        ),
    )
    parser.add_argument(
        "--static",
        action="store_true",
        help="Use static benchmark questions instead of resolving live date placeholders.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Regenerate reports that already exist and are non-empty.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Load and select questions without calling search or model APIs.",
    )
    args = parser.parse_args()

    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.max_concurrent < 1:
        parser.error("--max-concurrent must be at least 1")
    if args.progress_interval < 0:
        parser.error("--progress-interval cannot be negative")
    return args


def slugify(value: str) -> str:
    """Convert a model or system name into a safe directory name."""
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return slug or "unknown-model"


def default_model_name() -> str:
    """Build a descriptive output directory name from active configuration."""
    search_api = os.getenv("SEARCH_API", "tavily")
    research_model = os.getenv("RESEARCH_MODEL", "openai:gpt-4.1")
    return slugify(f"open-deep-research-{search_api}-{research_model}")


def select_questions(
    benchmark_data: dict[str, dict[str, Any]],
    qids: list[str] | None,
    limit: int | None,
) -> list[tuple[str, str]]:
    """Select benchmark questions while preserving dataset order."""
    requested = None
    if qids:
        requested = {qid.removeprefix("qid_") for qid in qids}
        missing = requested.difference(benchmark_data)
        if missing:
            missing_text = ", ".join(sorted(missing))
            raise ValueError(f"Unknown LiveResearchBench query IDs: {missing_text}")

    selected = [
        (qid, str(item.get("question", "")).strip())
        for qid, item in benchmark_data.items()
        if requested is None or qid in requested
    ]
    selected = [(qid, question) for qid, question in selected if question]
    if limit is not None:
        selected = selected[:limit]
    return selected


def validate_environment() -> Configuration:
    """Validate the effective research configuration without making API calls."""
    config = Configuration.from_runnable_config(
        {"configurable": {"allow_clarification": False}}
    )

    if config.allow_clarification:
        raise ValueError(
            "LiveResearchBench requires ALLOW_CLARIFICATION=false so every "
            "single-turn question produces a report"
        )
    if os.getenv("GET_API_KEYS_FROM_CONFIG", "false").lower() == "true":
        raise ValueError(
            "This standalone runner requires GET_API_KEYS_FROM_CONFIG=false "
            "so it can read API keys from .env"
        )

    if config.search_api.value == "tavily" and not os.getenv("TAVILY_API_KEY"):
        raise ValueError("TAVILY_API_KEY is required when SEARCH_API=tavily")

    model_names = {
        config.summarization_model,
        config.research_model,
        config.compression_model,
        config.final_report_model,
    }
    if any(model.startswith("openai:") for model in model_names):
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY is required for openai:* models")

    return config


def write_report_atomically(path: Path, content: str) -> None:
    """Write a completed report without leaving a partial target file."""
    temporary_path = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary_path.write_text(content, encoding="utf-8")
    temporary_path.replace(path)


def write_json_atomically(path: Path, value: dict[str, Any]) -> None:
    """Write formatted JSON without leaving a partial target file."""
    content = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    write_report_atomically(path, content)


def append_event(path: Path, event: dict[str, Any]) -> None:
    """Append one resumable run event as JSONL."""
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event, ensure_ascii=False) + "\n")
        file.flush()
        os.fsync(file.fileno())


def beijing_now() -> datetime:
    """Return the current timezone-aware Beijing time."""
    return datetime.now(BEIJING_TZ)


def beijing_time_text() -> str:
    """Format the current Beijing time for console progress messages."""
    return beijing_now().strftime("%Y-%m-%d %H:%M:%S CST")


async def generate_reports(args: argparse.Namespace) -> int:
    """Generate the selected reports and return a process exit code."""
    use_realtime = not args.static
    benchmark_data = load_liveresearchbench_dataset(use_realtime=use_realtime)
    if not benchmark_data:
        raise RuntimeError("LiveResearchBench dataset could not be loaded")

    selected = select_questions(benchmark_data, args.qid, args.limit)
    if not selected:
        raise ValueError("No LiveResearchBench questions were selected")

    model_name = slugify(args.model_name) if args.model_name else default_model_name()
    model_dir = args.output_dir.resolve() / model_name

    print(f"Loaded questions: {len(benchmark_data)}")
    print(f"Selected questions: {len(selected)}")
    print(f"Realtime questions: {use_realtime}")
    print(f"Output directory: {model_dir}")

    if args.dry_run:
        for qid, question in selected:
            print(f"- {qid}: {question[:120]}")
        return 0

    effective_config = validate_environment()
    print(f"Search API: {effective_config.search_api.value}")
    print(f"Research model: {effective_config.research_model}")
    print(f"Outer concurrency: {args.max_concurrent}")
    print(
        "Inner researcher concurrency: "
        f"{effective_config.max_concurrent_research_units}"
    )
    print("Token usage: API-reported usage only (no local estimation)")

    model_dir.mkdir(parents=True, exist_ok=True)
    events_path = model_dir / "run_events.jsonl"
    event_lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(args.max_concurrent)
    graph = deep_researcher_builder.compile(checkpointer=MemorySaver())
    batch_started = time.monotonic()
    finished_count = 0

    async def record_event(event: dict[str, Any]) -> None:
        async with event_lock:
            append_event(events_path, event)

    async def run_one(
        position: int, qid: str, question: str
    ) -> tuple[str, str, float]:
        report_path = model_dir / f"qid_{qid}_report.md"
        stats_path = model_dir / f"qid_{qid}_stats.json"
        trace_path = model_dir / f"qid_{qid}_llm_trace.jsonl"
        if report_path.exists() and report_path.stat().st_size > 0 and not args.overwrite:
            if not stats_path.exists() or stats_path.stat().st_size == 0:
                return qid, "skipped (stats missing; use --overwrite to regenerate)", 0.0
            if not trace_path.is_file():
                return qid, "skipped (trace missing; use --overwrite to regenerate)", 0.0
            return qid, "skipped", 0.0

        async with semaphore:
            started = time.monotonic()
            run_id = uuid.uuid4().hex
            print(
                f"[{beijing_time_text()}] [start {position}/{len(selected)}] {qid}; "
                f"finished={finished_count}, remaining={len(selected) - finished_count}",
                flush=True,
            )
            await record_event(
                {
                    "run_id": run_id,
                    "timestamp": beijing_now().isoformat(),
                    "query_id": qid,
                    "status": "started",
                    "position": position,
                    "total_questions": len(selected),
                }
            )

            async def report_progress() -> None:
                if args.progress_interval == 0:
                    return
                while True:
                    await asyncio.sleep(args.progress_interval)
                    elapsed = time.monotonic() - started
                    print(
                        f"[{beijing_time_text()}] "
                        f"[running {position}/{len(selected)}] {qid}; "
                        f"elapsed={elapsed:.1f}s, finished={finished_count}, "
                        f"remaining={len(selected) - finished_count}",
                        flush=True,
                    )

            progress_task = asyncio.create_task(report_progress())
            stats = ResearchStatsCallback(session_id=run_id)
            try:
                result = await graph.ainvoke(
                    {"messages": [{"role": "user", "content": question}]},
                    {
                        "configurable": {
                            "thread_id": str(uuid.uuid4()),
                            "allow_clarification": False,
                        },
                        "callbacks": [stats],
                        "recursion_limit": 100,
                    },
                )
                summary = stats.summary()
                report = str(result.get("final_report", "")).strip()
                research_brief = str(result.get("research_brief", "")).strip()
                raw_notes = result.get("raw_notes", [])
                validation_errors = []
                if not research_brief:
                    validation_errors.append("research_brief is empty")
                if not any(str(note).strip() for note in raw_notes):
                    validation_errors.append("no research notes were produced")
                if (
                    effective_config.search_api.value == "tavily"
                    and summary.get("total_search_count", 0) <= 0
                ):
                    validation_errors.append("no Tavily search was performed")
                if not report:
                    validation_errors.append("final report is empty")
                elif report.startswith("Error generating final report"):
                    validation_errors.append("final report generation failed")
                if validation_errors:
                    raise RuntimeError(
                        "invalid research run: " + "; ".join(validation_errors)
                    )

                elapsed = time.monotonic() - started
                raw_context = "\n".join(
                    str(note) for note in result.get("raw_notes", [])
                )
                summary.update(
                    {
                        "run_id": run_id,
                        "status": "completed",
                        "qid": qid,
                        "query": question,
                        "duration_seconds": round(elapsed, 3),
                        "report_length": len(report),
                        "context_length": len(raw_context),
                        "source_urls_count": len(
                            {
                                item.get("url")
                                for call in summary["search_calls_detail"]
                                for item in call.get("results", [])
                                if item.get("url")
                            }
                        ),
                        "token_counting": (
                            "Token counts come only from API-reported usage; "
                            "missing usage is never estimated."
                        ),
                    }
                )
                write_report_atomically(report_path, report + "\n")
                write_json_atomically(stats_path, summary)
                stats.write_trace(trace_path)
                await record_event(
                    {
                        "run_id": run_id,
                        "timestamp": beijing_now().isoformat(),
                        "query_id": qid,
                        "status": "completed",
                        "elapsed_seconds": round(elapsed, 3),
                        "report_file_path": str(report_path),
                        "stats_file_path": str(stats_path),
                        "trace_file_path": str(trace_path),
                    }
                )
                return qid, "completed", elapsed
            except (Exception, TavilyUsageLimitExceeded) as exc:
                elapsed = time.monotonic() - started
                failure_dir = model_dir / "failed"
                failure_dir.mkdir(parents=True, exist_ok=True)
                failure_trace_path = (
                    failure_dir / f"qid_{qid}_{run_id}_llm_trace.jsonl"
                )
                stats.write_trace(failure_trace_path)
                failure_path = failure_dir / f"qid_{qid}_{run_id}_failure.json"
                failure = stats.summary()
                failure.update(
                    {
                        "run_id": run_id,
                        "status": "failed",
                        "qid": qid,
                        "query": question,
                        "duration_seconds": round(elapsed, 3),
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "trace_file_path": str(failure_trace_path),
                    }
                )
                write_json_atomically(failure_path, failure)
                await record_event(
                    {
                        "run_id": run_id,
                        "timestamp": beijing_now().isoformat(),
                        "query_id": qid,
                        "status": "failed",
                        "elapsed_seconds": round(elapsed, 3),
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "failure_file_path": str(failure_path),
                        "trace_file_path": str(failure_trace_path),
                    }
                )
                if isinstance(exc, TavilyUsageLimitExceeded):
                    raise
                return qid, f"failed: {type(exc).__name__}: {exc}", elapsed
            finally:
                progress_task.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await progress_task

    tasks = [
        asyncio.create_task(run_one(position, qid, question))
        for position, (qid, question) in enumerate(selected, start=1)
    ]
    completed = 0
    skipped = 0
    failed = 0

    for future in asyncio.as_completed(tasks):
        qid, status, elapsed = await future
        if status == "completed":
            completed += 1
        elif status.startswith("skipped"):
            skipped += 1
        else:
            failed += 1
        finished_count += 1
        print(
            f"[{beijing_time_text()}] "
            f"[{completed + skipped + failed}/{len(tasks)}] "
            f"{qid}: {status} ({elapsed:.1f}s); "
            f"remaining={len(tasks) - finished_count}",
            flush=True,
        )

    batch_elapsed = time.monotonic() - batch_started
    print(
        f"[{beijing_time_text()}] Finished: completed={completed}, "
        f"skipped={skipped}, failed={failed}, "
        f"elapsed={batch_elapsed:.1f}s, output={model_dir}"
    )
    return 1 if failed else 0


def main() -> int:
    """Run the asynchronous report generator."""
    args = parse_args()
    try:
        return asyncio.run(generate_reports(args))
    except TavilyUsageLimitExceeded as exc:
        print(
            "Tavily usage limit exhausted. Update TAVILY_API_KEY in .env and "
            f"rerun the same command. Tavily response: {exc}",
            file=sys.stderr,
        )
        return 1
    except KeyboardInterrupt:
        print("Interrupted; completed reports remain resumable.", file=sys.stderr)
        return 130
    except Exception as exc:
        print(f"Error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
'''
python run_liveresearch_bench.py \
    --model-name "bailian-deepseek-v4-flash-0731-260823-0349" \
    --output-dir "outputs/liveresearchbench" \
    --limit 1 \
    --qid "market6VWmPyxptfK47civ"
'''
