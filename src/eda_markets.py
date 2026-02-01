import json
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main() -> None:
    out_dir = Path("results")
    figs_dir = Path("figures")
    figs_dir.mkdir(exist_ok=True)

    markets_path = out_dir / "markets.jsonl"
    rows = load_jsonl(markets_path)
    df = pd.DataFrame(rows)

    stats = {
        "count": int(len(df)),
        "missing_probability": int(df["probability"].isna().sum()),
        "probability_mean": float(df["probability"].mean()),
        "probability_std": float(df["probability"].std()),
        "probability_min": float(df["probability"].min()),
        "probability_max": float(df["probability"].max()),
    }

    with (out_dir / "markets_stats.json").open("w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    # Distribution plot
    plt.figure(figsize=(6, 4))
    plt.hist(df["probability"].dropna(), bins=20, color="#4C72B0")
    plt.title("Market Probability Distribution")
    plt.xlabel("Probability")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(figs_dir / "market_probability_hist.png", dpi=150)
    plt.close()

    df.to_csv(out_dir / "markets_table.csv", index=False)


if __name__ == "__main__":
    main()
