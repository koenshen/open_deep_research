#!/usr/bin/env python3
"""Generate Open Deep Research reports for Deep Research Bench."""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import json
import os
import sys
import time
import uuid
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_BENCHMARK_DIR = PROJECT_ROOT.parent / "deep_research_bench"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs" / "deepresearchbench"

load_dotenv(PROJECT_ROOT / ".env")

from open_deep_research.configuration import Configuration  # noqa: E402
from open_deep_research.deep_researcher import deep_researcher_builder  # noqa: E402
from open_deep_research.utils import TavilyUsageLimitExceeded  # noqa: E402
from liveresearchbench_stats import ResearchStatsCallback  # noqa: E402


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Run Open Deep Research on Deep Research Bench questions and emit "
            "the JSONL format consumed by its RACE and FACT evaluators."
        )
    )
    parser.add_argument("--benchmark-dir", type=Path, default=DEFAULT_BENCHMARK_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--model-name", default="open-deep-research")
    parser.add_argument(
        "--id", action="append", dest="ids", help="Select one task ID; repeatable."
    )
    parser.add_argument("--limit", type=int, help="Run only the first N selected tasks.")
    parser.add_argument("--max-concurrent", type=int, default=1)
    parser.add_argument("--progress-interval", type=float, default=30.0)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be at least 1")
    if args.max_concurrent < 1:
        parser.error("--max-concurrent must be at least 1")
    if args.progress_interval < 0:
        parser.error("--progress-interval cannot be negative")
    return args


def slugify(value: str) -> str:
    """Return a filesystem-safe model name."""
    import re

    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return slug or "open-deep-research"


def load_tasks(query_file: Path) -> list[dict[str, Any]]:
    """Load and minimally validate the benchmark query JSONL."""
    if not query_file.is_file():
        raise FileNotFoundError(f"Benchmark query file not found: {query_file}")
    tasks = []
    with query_file.open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            item = json.loads(line)
            if "id" not in item or not str(item.get("prompt", "")).strip():
                raise ValueError(f"Invalid task at {query_file}:{line_number}")
            tasks.append(item)
    if not tasks:
        raise ValueError(f"No tasks found in {query_file}")
    return tasks


def select_tasks(
    tasks: list[dict[str, Any]], ids: list[str] | None, limit: int | None
) -> list[dict[str, Any]]:
    """Select tasks in dataset order."""
    requested = set(ids or [])
    known = {str(item["id"]) for item in tasks}
    missing = requested - known
    if missing:
        raise ValueError(f"Unknown task IDs: {', '.join(sorted(missing))}")
    selected = [item for item in tasks if not requested or str(item["id"]) in requested]
    return selected[:limit] if limit is not None else selected


def validate_environment() -> Configuration:
    """Validate effective agent configuration without calling external APIs."""
    config = Configuration.from_runnable_config(
        {"configurable": {"allow_clarification": False}}
    )
    if os.getenv("GET_API_KEYS_FROM_CONFIG", "false").lower() == "true":
        raise ValueError("Set GET_API_KEYS_FROM_CONFIG=false for this standalone runner")
    if config.search_api.value == "tavily" and not os.getenv("TAVILY_API_KEY"):
        raise ValueError("TAVILY_API_KEY is required when SEARCH_API=tavily")
    models = {
        config.summarization_model,
        config.research_model,
        config.compression_model,
        config.final_report_model,
    }
    if any(model.startswith("openai:") for model in models) and not os.getenv(
        "OPENAI_API_KEY"
    ):
        raise ValueError("OPENAI_API_KEY is required for openai:* models")
    return config


def write_text_atomically(path: Path, content: str) -> None:
    """Write a file without exposing a partial destination."""
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def rebuild_submission(tasks: list[dict[str, Any]], model_dir: Path, path: Path) -> int:
    """Rebuild the ordered benchmark submission from completed reports."""
    rows = []
    for task in tasks:
        report_path = model_dir / f"task_{task['id']}_report.md"
        if report_path.is_file() and report_path.stat().st_size:
            rows.append(
                {
                    "id": task["id"],
                    "prompt": task["prompt"],
                    "article": report_path.read_text(encoding="utf-8").strip(),
                }
            )
    content = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    write_text_atomically(path, content)
    return len(rows)


def append_submission_row(path: Path, row: dict[str, Any]) -> None:
    """Append one completed evaluator row and flush it durably."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(row, ensure_ascii=False) + "\n")
        file.flush()
        os.fsync(file.fileno())


async def generate_reports(args: argparse.Namespace) -> int:
    """Generate selected reports and return a process exit code."""
    query_file = args.benchmark_dir.resolve() / "data" / "prompt_data" / "query.jsonl"
    all_tasks = load_tasks(query_file)
    selected = select_tasks(all_tasks, args.ids, args.limit)
    model_name = slugify(args.model_name)
    model_dir = args.output_dir.resolve() / model_name
    submission_path = model_dir / f"{model_name}.jsonl"

    print(f"Loaded tasks: {len(all_tasks)}")
    print(f"Selected tasks: {len(selected)}")
    print(f"Output directory: {model_dir}")
    print(f"Submission JSONL: {submission_path}")
    if args.dry_run:
        for task in selected:
            print(f"- {task['id']} [{task.get('language', '?')}]: {task['prompt'][:120]}")
        return 0

    config = validate_environment()
    print(f"Search API: {config.search_api.value}")
    print(f"Research model: {config.research_model}")
    print(f"Outer concurrency: {args.max_concurrent}")
    model_dir.mkdir(parents=True, exist_ok=True)
    events_path = model_dir / "run_events.jsonl"
    semaphore = asyncio.Semaphore(args.max_concurrent)
    event_lock = asyncio.Lock()
    submission_lock = asyncio.Lock()
    graph = deep_researcher_builder.compile(checkpointer=MemorySaver())
    rebuild_submission(all_tasks, model_dir, submission_path)
    submission_ids = {
        task["id"]
        for task in all_tasks
        if (
            (model_dir / f"task_{task['id']}_report.md").is_file()
            and (model_dir / f"task_{task['id']}_report.md").stat().st_size
        )
    }

    async def event(value: dict[str, Any]) -> None:
        async with event_lock:
            with events_path.open("a", encoding="utf-8") as file:
                file.write(json.dumps(value, ensure_ascii=False) + "\n")
                file.flush()
                os.fsync(file.fileno())

    async def run_one(task: dict[str, Any]) -> tuple[Any, str]:
        task_id = task["id"]
        report_path = model_dir / f"task_{task_id}_report.md"
        stats_path = model_dir / f"task_{task_id}_stats.json"
        trace_path = model_dir / f"task_{task_id}_llm_trace.jsonl"
        if (
            report_path.is_file()
            and report_path.stat().st_size
            and stats_path.is_file()
            and stats_path.stat().st_size
            and trace_path.is_file()
            and not args.overwrite
        ):
            return task_id, "skipped"
        async with semaphore:
            started = time.monotonic()
            run_id = uuid.uuid4().hex
            print(f"[start] task {task_id}", flush=True)
            await event(
                {
                    "run_id": run_id,
                    "task_id": task_id,
                    "status": "started",
                    "timestamp": time.time(),
                }
            )
            stats = ResearchStatsCallback(session_id=run_id)

            async def heartbeat() -> None:
                if args.progress_interval == 0:
                    return
                while True:
                    await asyncio.sleep(args.progress_interval)
                    print(
                        f"[running] task {task_id}; elapsed={time.monotonic()-started:.1f}s",
                        flush=True,
                    )

            progress = asyncio.create_task(heartbeat())
            try:
                result = await graph.ainvoke(
                    {"messages": [{"role": "user", "content": task["prompt"]}]},
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
                    config.search_api.value == "tavily"
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
                summary.update(
                    {
                        "run_id": run_id,
                        "status": "completed",
                        "id": task_id,
                        "prompt": task["prompt"],
                        "language": task.get("language"),
                        "topic": task.get("topic"),
                        "duration_seconds": round(elapsed, 3),
                        "report_length": len(report),
                        "context_length": len(
                            "\n".join(str(note) for note in result.get("raw_notes", []))
                        ),
                        "source_urls_count": len(
                            {
                                item.get("url")
                                for call in summary["search_calls_detail"]
                                for item in call.get("results", [])
                                if item.get("url")
                            }
                        ),
                    }
                )
                write_text_atomically(report_path, report + "\n")
                write_text_atomically(
                    stats_path, json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
                )
                stats.write_trace(trace_path)
                async with submission_lock:
                    if task_id not in submission_ids:
                        append_submission_row(
                            submission_path,
                            {
                                "id": task_id,
                                "prompt": task["prompt"],
                                "article": report,
                            },
                        )
                        submission_ids.add(task_id)
                await event(
                    {
                        "run_id": run_id,
                        "task_id": task_id,
                        "status": "completed",
                        "elapsed_seconds": round(elapsed, 3),
                        "report_file_path": str(report_path),
                        "stats_file_path": str(stats_path),
                        "trace_file_path": str(trace_path),
                    }
                )
                return task_id, "completed"
            except (Exception, TavilyUsageLimitExceeded) as exc:
                elapsed = time.monotonic() - started
                failure_dir = model_dir / "failed"
                failure_dir.mkdir(parents=True, exist_ok=True)
                failure_trace_path = (
                    failure_dir / f"task_{task_id}_{run_id}_llm_trace.jsonl"
                )
                stats.write_trace(failure_trace_path)
                failure_path = failure_dir / f"task_{task_id}_{run_id}_failure.json"
                failure = stats.summary()
                failure.update(
                    {
                        "run_id": run_id,
                        "status": "failed",
                        "id": task_id,
                        "prompt": task["prompt"],
                        "language": task.get("language"),
                        "topic": task.get("topic"),
                        "duration_seconds": round(elapsed, 3),
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                        "trace_file_path": str(failure_trace_path),
                    }
                )
                write_text_atomically(
                    failure_path,
                    json.dumps(failure, ensure_ascii=False, indent=2) + "\n",
                )
                await event(
                    {
                        "run_id": run_id,
                        "task_id": task_id,
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
                return task_id, f"failed: {type(exc).__name__}: {exc}"
            finally:
                progress.cancel()
                with contextlib.suppress(asyncio.CancelledError):
                    await progress

    results = await asyncio.gather(*(run_one(task) for task in selected))
    for task_id, status in results:
        print(f"[result] task {task_id}: {status}")
    row_count = rebuild_submission(all_tasks, model_dir, submission_path)
    failures = [status for _, status in results if status.startswith("failed")]
    print(f"Submission rows: {row_count}/{len(all_tasks)}")
    return 1 if failures else 0


def main() -> int:
    """Run the asynchronous report generator."""
    try:
        return asyncio.run(generate_reports(parse_args()))
    except TavilyUsageLimitExceeded as exc:
        print(f"Tavily usage limit exhausted: {exc}", file=sys.stderr)
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
python run_deepresearch_bench.py \
    --model-name "aionly-deepseek-v4-flash-260823-1543" \
    --output-dir "outputs/deepresearchbench" \
    --id 1
'''
