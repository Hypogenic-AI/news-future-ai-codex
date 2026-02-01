# Planning: News from the Future

## Motivation & Novelty Assessment

### Why This Research Matters
LLM-generated "news from the future" could help analysts, policymakers, and the public explore plausible futures and prepare for contingencies. Combining LLMs with prediction markets may yield narratives that are both coherent and probabilistically grounded, improving trust and utility for decision-making and scenario planning.

### Gap in Existing Work
Prior work focuses on forecasting QA or short-form answers and on calibration benchmarks (e.g., Daily Oracle, ForecastQA, KalshiBench). There is limited evaluation of full news-style narratives, and market signals are rarely integrated into generation to shape uncertainty-aware storytelling.

### Our Novel Contribution
We test a lightweight, market-informed prompting method that injects real prediction-market probabilities into LLM news generation and evaluates whether this improves narrative plausibility and probabilistic alignment over a baseline without market signals.

### Experiment Justification
- Experiment 1 (Baseline vs Market-Informed generation): Needed to test whether market probabilities improve perceived plausibility and internal consistency of future-news narratives.
- Experiment 2 (Probability alignment analysis): Needed to quantify whether generated narratives better reflect market priors (calibration alignment) when market signals are provided.
- Experiment 3 (Error analysis): Needed to identify failure modes (e.g., hallucinated specifics, contradiction with market signal) and assess robustness.

---

## Research Question
Can combining LLMs with prediction-market probabilities generate more plausible and better-calibrated "news from the future" narratives than a baseline LLM without market signals?

## Background and Motivation
Forecasting benchmarks show LLMs degrade over time and struggle with calibration. Prediction markets aggregate dispersed information and provide probabilistic signals. A narrative generation system that incorporates market signals may produce more plausible and uncertainty-aware future news, addressing gaps in existing benchmarks that focus on QA rather than narrative plausibility.

## Hypothesis Decomposition
1. Market-informed prompts improve narrative plausibility vs. baseline prompts.
2. Market-informed prompts yield narratives whose implied probabilities align more closely with market probabilities.
3. Market-informed prompts reduce contradiction and overconfident language.

## Proposed Methodology

### Approach
Use a real prediction-market API to sample unresolved or recently resolved markets, then prompt an LLM to generate short "future news" articles with and without market probabilities. Evaluate plausibility and alignment using a separate LLM-as-judge rubric and numeric alignment metrics.

### Experimental Steps
1. Collect prediction-market questions and probabilities (Manifold API).
2. Sample a fixed set of markets and construct prompts for baseline and market-informed conditions.
3. Generate short news articles using an LLM API (OpenAI).
4. Evaluate outputs with a judge model for plausibility, coherence, and probability alignment.
5. Compute statistical comparisons and effect sizes between conditions.

### Baselines
- Baseline LLM prompt without market probability
- Market-informed LLM prompt with probability and implied probability request

### Evaluation Metrics
- LLM-judge plausibility score (1-5)
- Coherence score (1-5)
- Market alignment: absolute error between market prob and model-implied prob
- Linguistic uncertainty markers (hedging rate)

### Statistical Analysis Plan
- Paired t-test or Wilcoxon signed-rank test on plausibility and alignment metrics
- Effect size: Cohen's d for paired samples
- Significance level: alpha = 0.05

## Expected Outcomes
Support: Market-informed prompts show higher plausibility and lower probability alignment error. Refute: No significant differences or worse alignment.

## Timeline and Milestones
- Setup + data collection: 30-45 min
- Generation + evaluation: 60-90 min
- Analysis + visualization: 45-60 min
- Documentation: 30-45 min

## Potential Challenges
- Limited or noisy market data
- LLM judge bias
- Market probability not available historically

## Success Criteria
- Statistically significant improvement in plausibility and/or probability alignment
- Clear, reproducible pipeline with saved outputs and evaluation reports
