import json
import os
from pathlib import Path

from utils import call_model, ensure_openai_client, extract_json, safe_append_jsonl

MODEL = os.getenv("JUDGE_MODEL", "gpt-4.1")

SYSTEM_PROMPT = (
    "You are an expert editor evaluating future-news drafts. "
    "Score plausibility, coherence, and alignment with the provided probability."
)

JUDGE_TEMPLATE = """
Evaluate the article against the question and probability prior.
Provide JSON with keys: plausibility (1-5), coherence (1-5), alignment (1-5),
probability_error (0-1), contradictions (true/false), notes (string).

Question: {question}
Market probability prior: {probability:.3f}
Article:
{article}

Implied probability by author: {implied_probability}
"""


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    client = ensure_openai_client()
    out_dir = Path("results")
    baseline_path = out_dir / "articles_baseline.jsonl"
    market_path = out_dir / "articles_market.jsonl"

    if not baseline_path.exists() or not market_path.exists():
        raise FileNotFoundError("Missing article files; run generate_articles.py first")

    baseline = load_jsonl(baseline_path)
    market = load_jsonl(market_path)
    market_map = {m["id"]: m for m in market}

    out_path = out_dir / "judgments.jsonl"
    done_ids = set()
    if out_path.exists():
        with out_path.open("r", encoding="utf-8") as f:
            for line in f:
                done_ids.add(json.loads(line)["id"])

    for b in baseline:
        mid = b["id"]
        if mid in done_ids:
            continue
        m = market_map.get(mid)
        if not m:
            continue
        for condition, row in [("baseline", b), ("market", m)]:
            article = row["output"].get("article", "")
            implied_prob = row["output"].get("implied_probability", None)
            prob_prior = m.get("market_probability", m.get("probability", 0.5))
            prompt = JUDGE_TEMPLATE.format(
                question=row["question"],
                probability=float(prob_prior),
                article=article,
                implied_probability=implied_prob,
            )
            text = call_model(client, MODEL, SYSTEM_PROMPT, prompt, temperature=0.0)
            judge = extract_json(text)
            out_row = {
                "id": mid,
                "condition": condition,
                "model": MODEL,
                "judge": judge,
            }
            safe_append_jsonl(str(out_path), out_row)


if __name__ == "__main__":
    main()
