# Outline: News from the Future (NeurIPS-style)

## Title
- Market-Conditioned Prompting Improves Plausibility and Calibration of Future-News Narratives

## Abstract
- Problem: narrative forecasting needs plausibility + calibration; QA benchmarks do not address narratives.
- Gap: LLMs often overconfident; few methods inject probabilistic priors into narrative generation.
- Approach: pairwise baseline vs market-informed prompts on 30 Manifold markets; LLM judge for plausibility, coherence, alignment, probability error; paired t-tests + Cohen's d.
- Key results: plausibility +0.633 (p=4.28e-06, d=1.03), alignment +1.867 (p=8.19e-09, d=1.459), probability error -0.282 (p=3.58e-08, d=-1.354); coherence unchanged at ceiling; no significant length/hedging changes.
- Significance: prediction-market priors are a lightweight, effective control for uncertainty-aware narratives.

## 1. Introduction
- Hook: LLMs can generate future news, but narratives risk overconfidence and hallucinated specifics.
- Importance: scenario planning, policy, editorial exploration need believable uncertainty-aware narratives.
- Gap: forecasting benchmarks focus on QA, not narrative plausibility; market signals rarely used in generation.
- Approach: market-conditioned prompting + LLM judge; include method overview figure.
- Quantitative preview: +14.5% plausibility, +59.6% alignment, 0.282 absolute probability error drop to near-zero.
- Contributions (bullets): propose market-conditioned prompting for narrative forecasting; conduct paired evaluation on 30 markets; show large gains in plausibility/alignment without harming coherence/length; provide analysis and limitations.
- Citations: Daily Oracle, OpenForecast, OpenForesight, KalshiBench, ForecastQA, SCTc-TE, Wolfers & Zitzewitz.

## 2. Related Work
- Forecasting QA benchmarks: ForecastQA, Daily Oracle; limitation: short answers vs narratives.
- Open-ended forecasting datasets/methods: OpenForecast, OpenForesight; LLM eval methods.
- Prediction markets + calibration: KalshiBench; PM theory for prices as probabilities (Wolfers & Zitzewitz).
- Positioning: our work is narrative generation with explicit market priors.

## 3. Methodology
- Problem setup: given market question q and probability p, generate narrative y.
- Conditions: baseline prompt (no p) vs market-informed prompt (includes p); identical generation model.
- Dataset: 30 Manifold binary unresolved markets; collected 2026-02-01; fields and preprocessing steps.
- Evaluation: LLM judge scores plausibility, coherence, alignment; probability error metric; hedging rate per 100 words; word count.
- Stats: paired t-tests, Cohen's d.
- Implementation: models gpt-4.1 (generation + judge), temp 0.7/0.0, max_output_tokens 700; seed 42.

## 4. Results
- Table: main metrics (means, p-values, d, n=30) with bold best.
- Figures: probability distribution histogram; boxplots for plausibility, alignment, probability error.
- Analysis: strong improvements in plausibility/alignment; coherence ceiling (p=NaN); negligible length/hedging.
- Comparison to baseline: quantify deltas and effect sizes.

## 5. Discussion
- Interpretation: market priors anchor narratives to uncertainty; LLM judge alignment saturates at max.
- Limitations: small sample (n=30), single run, LLM judge bias, market niche coverage, no historical snapshots.
- Failure modes: baseline overconfident; market-informed sometimes repeats probability without causal detail.
- Broader implications: scenario planning, editorial tools; caution about misuse/overreliance on market priors.

## 6. Conclusion
- Summary: market-conditioned prompts improve plausibility and calibration in narrative forecasting.
- Key takeaway: prediction markets are effective priors for narrative generation.
- Future work: human eval, historical market snapshots, broader market sources, narrative tone calibration.

## Figures/Tables
- Table 1: main results metrics.
- Figure 1: method overview diagram (constructed in LaTeX).
- Figure 2: market probability histogram (PNG).
- Figure 3: plausibility boxplot (PNG).
- Figure 4: alignment boxplot (PNG).
- Figure 5: probability error boxplot (PNG).

## Citations (BibTeX keys)
- dai2025dailyoracle
- wang2025openforecast
- chandak2026openforecaster
- nel2025kalshibench
- zhang2021forecastqa
- wang2023sctcte
- wolfers2006theory
- wolfers2006prices
