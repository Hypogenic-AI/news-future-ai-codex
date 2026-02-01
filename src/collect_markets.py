import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import requests

from utils import utc_now_iso

MANIFOLD_API = "https://api.manifold.markets/v0/markets"


def fetch_markets(limit: int = 200) -> List[Dict[str, Any]]:
    # Manifold API parameters are minimal; filter open markets locally.
    params = {"limit": limit}
    resp = requests.get(MANIFOLD_API, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def filter_binary_open(markets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)
    filtered = []
    for m in markets:
        if m.get("outcomeType") != "BINARY":
            continue
        if m.get("isResolved"):
            continue
        close_time = m.get("closeTime")
        if not close_time or close_time <= now_ms:
            continue
        if m.get("probability") is None:
            continue
        filtered.append(m)
    return filtered


def main() -> None:
    random.seed(42)
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    markets = fetch_markets(limit=200)
    filtered = filter_binary_open(markets)

    random.shuffle(filtered)
    sample = filtered[:30]

    rows = []
    for m in sample:
        rows.append(
            {
                "id": m.get("id"),
                "question": m.get("question"),
                "probability": m.get("probability"),
                "close_time": m.get("closeTime"),
                "url": m.get("url"),
                "created_time": m.get("createdTime"),
                "collected_at": utc_now_iso(),
                "source": "manifold",
            }
        )

    out_path = out_dir / "markets.jsonl"
    with out_path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=True) + "\n")

    meta = {
        "count_raw": len(markets),
        "count_filtered": len(filtered),
        "count_sample": len(sample),
        "collected_at": utc_now_iso(),
    }
    with (out_dir / "markets_meta.json").open("w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)


if __name__ == "__main__":
    main()
