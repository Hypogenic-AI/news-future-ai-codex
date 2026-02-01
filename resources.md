# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project, including papers, datasets, and code repositories.

## Papers
Total papers downloaded: 8

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Are LLMs Prescient? | Dai et al. | 2025 | papers/2025_dai_daily_oracle.pdf | Daily news forecasting benchmark (Daily Oracle) |
| OpenForecast | Wang et al. | 2025 | papers/2025_openforecast_coling.pdf | Open-ended event forecasting dataset |
| Scaling Open-Ended Reasoning To Predict the Future | Chandak et al. | 2026 | papers/2025_openforecaster_arxiv2512.25070.pdf | OpenForesight dataset + RL training |
| KalshiBench | Nel | 2025 | papers/2025_kalshibench_arxiv2512.16030.pdf | Prediction market calibration benchmark |
| ForecastQA | Zhang et al. | 2021 | papers/2021_forecastqa_acl.pdf | Temporal forecasting QA dataset |
| SCTc-TE | Wang et al. | 2023 | papers/2023_sctcte_arxiv2312.01052.pdf | Temporal event forecasting benchmark |
| Prediction Markets in Theory and Practice | Wolfers & Zitzewitz | 2006 | papers/2006_prediction_markets_theory_practice_nber_w12083.pdf | PM theory overview |
| Interpreting Prediction Market Prices as Probabilities | Wolfers & Zitzewitz | 2006 | papers/2006_prediction_markets_probabilities_nber_w12200.pdf | PM price-as-probability basis |

See `papers/README.md` for detailed descriptions.

## Datasets
Total datasets downloaded: 1

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| ForecastQA | inLab / USC | Train 8,210; Dev 1,090; Test 1,092 | Forecasting QA | datasets/forecastqa/ | Downloaded and sampled |

Additional datasets with download instructions in `datasets/README.md`:
- Daily Oracle
- OpenForesight
- OpenForecast
- SCTc-TE (MidEast-TE, GDELT-TE)

## Code Repositories
Total repositories cloned: 3

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| scaling-forecasting-training | https://github.com/openforecaster/scaling-forecasting-training | OpenForesight question generation + RL training | code/openforecaster_scaling_forecasting/ | Includes qgen, retrieval, and evaluation scripts |
| Openforecast | https://github.com/miaomiao1215/Openforecast | OpenForecast dataset access | code/openforecast/ | Google Drive data link in README |
| GDELT-ComplexEvent | https://github.com/yecchen/GDELT-ComplexEvent | SCTc-TE dataset + LoGo model | code/gdelt-complexevent/ | Includes MidEast-TE & GDELT-TE zips |

See `code/README.md` for detailed descriptions.

## Resource Gathering Notes

### Search Strategy
- Manual search across PMLR, ACL Anthology, arXiv, NBER, HuggingFace, and GitHub.
- Focused on LLM forecasting datasets, open-ended event forecasting, and prediction market calibration.

### Selection Criteria
- Direct relevance to LLM forecasting from news or prediction-market signals.
- Availability of datasets/code for reproducible experiments.
- Mix of recent state-of-the-art and foundational prediction market theory.

### Challenges Encountered
- Paper-finder service was unavailable; manual search used instead.
- Some datasets are large or hosted externally (OpenForesight, OpenForecast) and were not fully downloaded.

### Gaps and Workarounds
- Narrative news generation datasets are scarce; rely on event-forecasting datasets and augment with generation pipelines.

## Recommendations for Experiment Design

1. **Primary dataset(s)**: OpenForesight (training), Daily Oracle and ForecastQA (evaluation), OpenForecast (complex event narratives).
2. **Baseline methods**: Closed-book LLM, BM25/embedding RAG, LoGo (structured events).
3. **Evaluation metrics**: Accuracy + calibration (Brier/ECE) + LLM-as-judge for open-ended outputs.
4. **Code to adapt/reuse**: `code/openforecaster_scaling_forecasting/` for question generation and evaluation; `code/gdelt-complexevent/` for structured event baselines.

## Research Execution Log (2026-02-01)

- Collected 30 unresolved binary markets from Manifold API for market priors.
- Generated paired future-news articles with `gpt-4.1`: baseline vs market-informed.
- Evaluated outputs with LLM-as-judge (plausibility, coherence, alignment).
- Saved outputs to `results/` and plots to `figures/`.
- Full analysis and conclusions in `REPORT.md`.
