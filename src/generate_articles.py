import json
import os
from pathlib import Path

from utils import call_model, ensure_openai_client, extract_json, parse_date_ms_to_iso, safe_append_jsonl

MODEL = os.getenv("NEWS_MODEL", "gpt-4.1")

SYSTEM_PROMPT = (
    "You are a careful journalist writing plausible future news. "
    "Write clearly, avoid sensationalism, and be explicit about uncertainty."
)

BASELINE_USER_TEMPLATE = """
Write a short future news article (120-180 words) about the following question.
Use the date {future_date} as the dateline. Do not mention prediction markets.
Return JSON with keys: headline, article, implied_probability (0-1), key_facts (list).
Question: {question}
"""

MARKET_USER_TEMPLATE = """
Write a short future news article (120-180 words) about the following question.
Use the date {future_date} as the dateline. Incorporate this prediction market probability as a prior: {probability:.3f}.
Be explicit about uncertainty. Do not claim certainty if the market probability is far from 0 or 1.
Return JSON with keys: headline, article, implied_probability (0-1), key_facts (list).
Question: {question}
"""


def load_markets(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    client = ensure_openai_client()
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    markets_path = out_dir / "markets.jsonl"
    if not markets_path.exists():
        raise FileNotFoundError("markets.jsonl not found; run collect_markets.py first")

    markets = load_markets(markets_path)

    baseline_path = out_dir / "articles_baseline.jsonl"
    market_path = out_dir / "articles_market.jsonl"

    done_baseline = set()
    done_market = set()
    if baseline_path.exists():
        with baseline_path.open("r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                done_baseline.add(obj["id"])
    if market_path.exists():
        with market_path.open("r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                done_market.add(obj["id"])

    for m in markets:
        future_date = parse_date_ms_to_iso(m["close_time"])
        if m["id"] not in done_baseline:
            # Baseline
            baseline_prompt = BASELINE_USER_TEMPLATE.format(
                future_date=future_date, question=m["question"]
            )
            baseline_text = call_model(
                client, MODEL, SYSTEM_PROMPT, baseline_prompt, temperature=0.7
            )
            baseline_json = extract_json(baseline_text)
            baseline_row = {
                "id": m["id"],
                "question": m["question"],
                "future_date": future_date,
                "condition": "baseline",
                "model": MODEL,
                "output": baseline_json,
            }
            safe_append_jsonl(str(baseline_path), baseline_row)

        if m["id"] not in done_market:
            # Market-informed
            market_prompt = MARKET_USER_TEMPLATE.format(
                future_date=future_date,
                probability=float(m["probability"]),
                question=m["question"],
            )
            market_text = call_model(
                client, MODEL, SYSTEM_PROMPT, market_prompt, temperature=0.7
            )
            market_json = extract_json(market_text)
            market_row = {
                "id": m["id"],
                "question": m["question"],
                "future_date": future_date,
                "condition": "market",
                "market_probability": m["probability"],
                "model": MODEL,
                "output": market_json,
            }
            safe_append_jsonl(str(market_path), market_row)


if __name__ == "__main__":
    main()
