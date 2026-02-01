import json
import os
import re
import time
from datetime import datetime, timezone
from typing import Any, Dict, Optional, Tuple

from openai import OpenAI

JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_openai_client() -> OpenAI:
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("OPENROUTER_API_KEY"):
        raise RuntimeError(
            "Missing OPENAI_API_KEY or OPENROUTER_API_KEY in environment."
        )
    # OpenAI client picks up OPENAI_API_KEY automatically.
    # If OPENROUTER_API_KEY is provided, users may set OPENAI_BASE_URL externally.
    return OpenAI()


def extract_json(text: str) -> Dict[str, Any]:
    match = JSON_RE.search(text)
    if not match:
        raise ValueError("No JSON object found in model output")
    return json.loads(match.group(0))


def call_model(
    client: OpenAI,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.7,
    max_output_tokens: int = 700,
    retries: int = 3,
    sleep_s: float = 2.0,
) -> str:
    last_err: Optional[Exception] = None
    for attempt in range(1, retries + 1):
        try:
            resp = client.responses.create(
                model=model,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature,
                max_output_tokens=max_output_tokens,
            )
            # New Responses API convenience
            if hasattr(resp, "output_text"):
                return resp.output_text
            # Fallback for different response structure
            if getattr(resp, "output", None):
                content = resp.output[0].content[0]
                if hasattr(content, "text"):
                    return content.text
            raise RuntimeError("Unexpected response format")
        except Exception as exc:  # pragma: no cover
            last_err = exc
            time.sleep(sleep_s * attempt)
    raise RuntimeError(f"Model call failed after {retries} attempts: {last_err}")


def parse_date_ms_to_iso(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).date().isoformat()


def hedging_rate(text: str) -> float:
    # Simple heuristic: count hedge tokens per 100 words
    tokens = re.findall(r"\b\w+\b", text.lower())
    if not tokens:
        return 0.0
    hedges = {"may", "might", "could", "likely", "possibly", "uncertain", "expected"}
    hedge_count = sum(1 for t in tokens if t in hedges)
    return (hedge_count / max(len(tokens), 1)) * 100


def safe_write_jsonl(path: str, rows: list[Dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")


def safe_append_jsonl(path: str, row: Dict[str, Any]) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=True) + "\n")
