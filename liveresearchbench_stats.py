"""Per-question LLM and Tavily statistics for the LiveResearchBench runner."""

from __future__ import annotations

import threading
import time
from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path
from typing import Any
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo

from langchain_core.callbacks import BaseCallbackHandler


BEIJING_TZ = ZoneInfo("Asia/Shanghai")


def _now_text() -> str:
    return datetime.now(BEIJING_TZ).isoformat()


def _json_safe(value: Any) -> Any:
    """Convert LangChain message objects into JSON-serializable values."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, UUID):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    model_dump = getattr(value, "model_dump", None)
    if callable(model_dump):
        try:
            return _json_safe(model_dump())
        except Exception:
            pass
    if hasattr(value, "__dict__"):
        return _json_safe(vars(value))
    return str(value)


class ResearchStatsCallback(BaseCallbackHandler):
    """Collect exact Tavily history and API-reported LLM token usage."""

    def __init__(self, session_id: str | None = None) -> None:
        self._lock = threading.Lock()
        self._pending_llm: dict[str, dict[str, Any]] = {}
        self._sequence = 0
        self._trace_index = 0
        self.session_id = session_id or uuid4().hex
        self.llm_calls: list[dict[str, Any]] = []
        self.search_calls: list[dict[str, Any]] = []
        self.trace_events: list[dict[str, Any]] = []

    def _next_sequence(self) -> int:
        with self._lock:
            self._sequence += 1
            return self._sequence

    def _next_trace_index(self) -> int:
        with self._lock:
            self._trace_index += 1
            return self._trace_index

    def on_chat_model_start(
        self,
        serialized: dict[str, Any],
        messages: list[list[Any]],
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        conversation = messages[0] if messages else []
        invocation = kwargs.get("invocation_params") or {}
        model = (
            invocation.get("model")
            or (metadata or {}).get("ls_model_name")
            or serialized.get("name")
            or serialized.get("id", ["unknown"])[-1]
        )
        pending = {
            "sequence": self._next_sequence(),
            "call_index": self._next_trace_index(),
            "started_at": _now_text(),
            "started_monotonic": time.monotonic(),
            "model": str(model),
            "message_count": len(conversation),
            "messages": _json_safe(conversation),
            "temperature": invocation.get("temperature"),
            "tags": _json_safe(tags or []),
            "metadata": _json_safe(metadata or {}),
            "parent_run_id": str(parent_run_id) if parent_run_id else None,
        }
        with self._lock:
            self._pending_llm[str(run_id)] = pending

    def on_llm_end(
        self,
        response: Any,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        **kwargs: Any,
    ) -> None:
        del parent_run_id, tags, kwargs
        with self._lock:
            pending = self._pending_llm.pop(str(run_id), None)
        pending = pending or {
            "sequence": self._next_sequence(),
            "call_index": self._next_trace_index(),
            "started_at": _now_text(),
            "started_monotonic": time.monotonic(),
            "model": "unknown",
            "message_count": 0,
            "messages": [],
            "temperature": None,
            "tags": [],
            "metadata": {},
            "parent_run_id": None,
        }

        generation = None
        if getattr(response, "generations", None) and response.generations[0]:
            generation = response.generations[0][0]
        message = getattr(generation, "message", None)
        response_metadata = getattr(message, "response_metadata", {}) or {}
        finish_reason = response_metadata.get("finish_reason")
        if finish_reason is None and generation is not None:
            finish_reason = (getattr(generation, "generation_info", None) or {}).get(
                "finish_reason"
            )

        usage = getattr(message, "usage_metadata", None) if message is not None else None
        usage_source = "AIMessage.usage_metadata"
        if hasattr(usage, "model_dump"):
            usage = usage.model_dump()
        if not isinstance(usage, dict):
            token_usage = (getattr(response, "llm_output", None) or {}).get(
                "token_usage"
            )
            if isinstance(token_usage, dict):
                usage = {
                    "input_tokens": token_usage.get("prompt_tokens"),
                    "output_tokens": token_usage.get("completion_tokens"),
                    "total_tokens": token_usage.get("total_tokens"),
                }
                usage_source = "LLMResult.llm_output.token_usage"

        input_tokens = usage.get("input_tokens") if isinstance(usage, dict) else None
        output_tokens = usage.get("output_tokens") if isinstance(usage, dict) else None
        total_tokens = usage.get("total_tokens") if isinstance(usage, dict) else None
        usage_available = all(
            isinstance(value, int)
            for value in (input_tokens, output_tokens, total_tokens)
        )

        detail = {
            "sequence": pending["sequence"],
            "status": "completed",
            "started_at": pending["started_at"],
            "completed_at": _now_text(),
            "duration_seconds": round(
                time.monotonic() - pending["started_monotonic"], 3
            ),
            "model": pending["model"],
            "input_tokens": input_tokens if usage_available else None,
            "output_tokens": output_tokens if usage_available else None,
            "total_tokens": total_tokens if usage_available else None,
            "message_count": pending["message_count"],
            "token_usage_source": usage_source if usage_available else "missing",
            "token_usage_available": usage_available,
            "token_usage_details": deepcopy(usage) if usage_available else None,
            "finish_reason": finish_reason,
        }
        trace_event = {
            "session_id": self.session_id,
            "call_index": pending["call_index"],
            "sequence": pending["sequence"],
            "purpose": pending["metadata"].get("langgraph_node")
            or (pending["tags"][0] if pending["tags"] else "llm_call"),
            "call_group": pending["metadata"].get("langgraph_node")
            or (pending["tags"][0] if pending["tags"] else "llm_call"),
            "attempt": 1,
            "parent_run_id": pending["parent_run_id"],
            "status": "completed",
            "started_at": pending["started_at"],
            "completed_at": detail["completed_at"],
            "duration_seconds": detail["duration_seconds"],
            "model": pending["model"],
            "temperature": pending["temperature"],
            "input": {"messages": pending["messages"]},
            "output": _json_safe(message or getattr(generation, "text", None)),
            "usage": _json_safe(usage),
            "finish_reason": finish_reason,
            "tags": pending["tags"],
            "metadata": pending["metadata"],
            "classification": {
                "has_tool_call": bool(getattr(message, "tool_calls", None)),
                "has_answer": bool(
                    isinstance(getattr(message, "content", None), str)
                    and getattr(message, "content", "")
                ),
                "valid_protocol_response": True,
            },
        }
        with self._lock:
            self.llm_calls.append(detail)
            self.trace_events.append(trace_event)

    def on_llm_error(
        self,
        error: BaseException,
        *,
        run_id: UUID,
        parent_run_id: UUID | None = None,
        tags: list[str] | None = None,
        **kwargs: Any,
    ) -> None:
        del parent_run_id, tags, kwargs
        with self._lock:
            pending = self._pending_llm.pop(str(run_id), None)
        if pending is None:
            return
        detail = {
            "sequence": pending["sequence"],
            "status": "failed",
            "started_at": pending["started_at"],
            "completed_at": _now_text(),
            "duration_seconds": round(
                time.monotonic() - pending["started_monotonic"], 3
            ),
            "model": pending["model"],
            "input_tokens": None,
            "output_tokens": None,
            "total_tokens": None,
            "message_count": pending["message_count"],
            "token_usage_source": "missing",
            "token_usage_available": False,
            "token_usage_details": None,
            "error_type": type(error).__name__,
            "error": str(error),
        }
        trace_event = {
            "session_id": self.session_id,
            "call_index": pending["call_index"],
            "sequence": pending["sequence"],
            "purpose": pending["metadata"].get("langgraph_node")
            or (pending["tags"][0] if pending["tags"] else "llm_call"),
            "call_group": pending["metadata"].get("langgraph_node")
            or (pending["tags"][0] if pending["tags"] else "llm_call"),
            "attempt": 1,
            "parent_run_id": pending["parent_run_id"],
            "status": "failed",
            "started_at": pending["started_at"],
            "completed_at": detail["completed_at"],
            "duration_seconds": detail["duration_seconds"],
            "model": pending["model"],
            "temperature": pending["temperature"],
            "input": {"messages": pending["messages"]},
            "output": None,
            "usage": None,
            "tags": pending["tags"],
            "metadata": pending["metadata"],
            "error_type": type(error).__name__,
            "error": str(error),
            "classification": {
                "has_tool_call": False,
                "has_answer": False,
                "valid_protocol_response": False,
            },
        }
        with self._lock:
            self.llm_calls.append(detail)
            self.trace_events.append(trace_event)

    def on_custom_event(
        self,
        name: str,
        data: Any,
        *,
        run_id: UUID,
        tags: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        del run_id, tags, metadata, kwargs
        if name != "tavily_search_completed" or not isinstance(data, dict):
            return
        detail = deepcopy(data)
        detail["sequence"] = self._next_sequence()
        detail["timestamp"] = _now_text()
        with self._lock:
            self.search_calls.append(detail)

    def summary(self) -> dict[str, Any]:
        """Return a stable snapshot matching GPT Researcher's main fields."""
        with self._lock:
            llm_calls = sorted(deepcopy(self.llm_calls), key=lambda item: item["sequence"])
            search_calls = sorted(
                deepcopy(self.search_calls), key=lambda item: item["sequence"]
            )
        calls_with_usage = [
            call for call in llm_calls if call.get("token_usage_available")
        ]
        usage_complete = len(calls_with_usage) == len(llm_calls)
        counted_input = sum(int(call["input_tokens"]) for call in calls_with_usage)
        counted_output = sum(int(call["output_tokens"]) for call in calls_with_usage)
        counted_total = sum(int(call["total_tokens"]) for call in calls_with_usage)
        visit_calls = []
        source_urls: set[str] = set()
        for search in search_calls:
            for result in search.get("results", []):
                url = result.get("url")
                if url:
                    source_urls.add(url)
                visit_calls.append(
                    {
                        "url": url,
                        "status": result.get("content_fetch_status", "missing"),
                        "content_length": int(result.get("raw_content_length", 0)),
                        "duration_seconds": search.get("duration_seconds"),
                        "query": search.get("query"),
                    }
                )
        visit_success = sum(item["status"] == "success" for item in visit_calls)
        return {
            "session_id": self.session_id,
            "total_llm_calls": len(llm_calls),
            "llm_calls_with_token_usage": len(calls_with_usage),
            "llm_calls_missing_token_usage": len(llm_calls) - len(calls_with_usage),
            "token_usage_complete": usage_complete,
            "total_input_tokens": counted_input if usage_complete else None,
            "total_output_tokens": counted_output if usage_complete else None,
            "total_tokens": counted_total if usage_complete else None,
            "counted_input_tokens": counted_input,
            "counted_output_tokens": counted_output,
            "counted_total_tokens": counted_total,
            "total_search_count": len(search_calls),
            "total_search_results": sum(
                int(call.get("num_results", 0)) for call in search_calls
            ),
            "total_visit_count": len(visit_calls),
            "total_visit_success": visit_success,
            "total_visit_failed": len(visit_calls) - visit_success,
            "source_urls_count": len(source_urls),
            "llm_calls_detail": llm_calls,
            "search_calls_detail": search_calls,
            "visit_calls_detail": visit_calls,
        }

    def write_trace(self, path: Path) -> None:
        """Persist the per-question LLM trace as JSONL."""
        with self._lock:
            events = sorted(deepcopy(self.trace_events), key=lambda item: item["sequence"])
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(f".{path.name}.{uuid4().hex}.tmp")
        with temporary.open("w", encoding="utf-8") as file:
            for event in events:
                file.write(json.dumps(event, ensure_ascii=False) + "\n")
        temporary.replace(path)
