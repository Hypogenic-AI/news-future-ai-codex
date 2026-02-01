import json
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats

from utils import hedging_rate


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

    baseline = load_jsonl(out_dir / "articles_baseline.jsonl")
    market = load_jsonl(out_dir / "articles_market.jsonl")
    judgments = load_jsonl(out_dir / "judgments.jsonl")

    def to_df(articles, condition):
        rows = []
        for r in articles:
            article = r["output"].get("article", "")
            implied = r["output"].get("implied_probability", None)
            rows.append(
                {
                    "id": r["id"],
                    "condition": condition,
                    "implied_probability": float(implied) if implied is not None else np.nan,
                    "hedging_rate": hedging_rate(article),
                    "word_count": len(article.split()),
                }
            )
        return pd.DataFrame(rows)

    df_articles = pd.concat(
        [to_df(baseline, "baseline"), to_df(market, "market")], ignore_index=True
    )

    df_j = pd.DataFrame(
        [
            {
                "id": j["id"],
                "condition": j["condition"],
                "plausibility": j["judge"].get("plausibility"),
                "coherence": j["judge"].get("coherence"),
                "alignment": j["judge"].get("alignment"),
                "probability_error": j["judge"].get("probability_error"),
                "contradictions": j["judge"].get("contradictions"),
            }
            for j in judgments
        ]
    )

    df = df_articles.merge(df_j, on=["id", "condition"], how="left")

    # Paired comparisons
    pivot = df.pivot(index="id", columns="condition")

    results = {}
    for metric in [
        "plausibility",
        "coherence",
        "alignment",
        "probability_error",
        "hedging_rate",
        "word_count",
    ]:
        if (metric, "baseline") not in pivot.columns or (metric, "market") not in pivot.columns:
            continue
        base = pivot[(metric, "baseline")].dropna()
        mark = pivot[(metric, "market")].dropna()
        common = base.index.intersection(mark.index)
        base = base.loc[common]
        mark = mark.loc[common]
        if len(common) < 5:
            continue
        t_stat, p_val = stats.ttest_rel(mark, base)
        diff = (mark - base).dropna()
        diff_std = diff.std(ddof=1)
        d = float(diff.mean() / diff_std) if diff_std and diff_std > 0 else 0.0
        results[metric] = {
            "n": int(len(common)),
            "baseline_mean": float(base.mean()),
            "market_mean": float(mark.mean()),
            "t_stat": float(t_stat),
            "p_value": float(p_val),
            "cohens_d": d,
        }

    with (out_dir / "stats.json").open("w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Plots
    sns.set_theme(style="whitegrid")
    for metric in ["plausibility", "coherence", "alignment", "probability_error"]:
        if metric not in df.columns:
            continue
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=df, x="condition", y=metric)
        plt.title(f"{metric.title()} by Condition")
        plt.tight_layout()
        plt.savefig(figs_dir / f"{metric}_boxplot.png", dpi=150)
        plt.close()

    # Save merged dataframe
    df.to_csv(out_dir / "analysis_table.csv", index=False)


if __name__ == "__main__":
    main()
