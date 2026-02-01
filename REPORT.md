# REPORT: News from the Future

## 1. Executive Summary
This study tests whether adding prediction-market probabilities to LLM prompts produces more plausible and better-calibrated future-news narratives than a baseline prompt without market signals. Across 30 paired markets, market-informed prompts significantly improved plausibility and alignment scores while reducing probability error, with no meaningful change in coherence or length. These results suggest prediction-market signals can be a useful prior for generating uncertainty-aware future news narratives.

## 2. Goal
**Hypothesis**: Combining LLMs with prediction-market probabilities can generate plausible news articles about future events, and those narratives will be better aligned with probabilistic priors than baseline LLM outputs.

**Importance**: Forecasting QA benchmarks evaluate short answers, not full news-style narratives. Narrative generation is more aligned with how humans consume future scenarios, but it is vulnerable to overconfidence and hallucinated specifics. Prediction markets provide probabilistic priors that may anchor narratives to real-world uncertainty.

**Expected impact**: A system that writes plausible "news from the future" could be valuable for scenario planning, policy analysis, and editorial exploration of uncertain events.

## 3. Data Construction

### Dataset Description
- **Source**: Manifold Markets public API (`/v0/markets`)
- **Type**: Binary, unresolved prediction markets with future close dates
- **Sample size**: 30 markets collected; 30 paired samples used in analysis
- **Collected**: 2026-02-01 (UTC)
- **Location**: `results/markets.jsonl`

### Example Samples
| Market Question | Baseline Headline | Market-Informed Headline |
|---|---|---|
| Impala Platinum Two PGM 6E Production 2027 | Impala Platinum Reports Mixed PGM 6E Production Figures for Early 2027 | Uncertainty Remains Over Impala Platinum's 2027 PGM 6E Production Targets |
| Impala Platinum Zimplats PGM 6E Production 2027 | Zimplats Reports Stable PGM 6E Production in Early 2027 | Outlook Unclear for Zimplats 2027 6E PGM Production as Market Signals 47% Probability |
| Will Moltbook be TIME person of the year 2026? | Moltbook Not Selected as TIME Person of the Year 2026 | Moltbook Unlikely to Be TIME Person of the Year, Say Observers |

### Data Quality
- **Missing values**: 0% missing probabilities
- **Probability range**: min 0.047, max 0.944
- **Mean probability**: 0.481 (std 0.233)
- **Quality checks**: verified open, unresolved, future close times; dropped markets missing probability

### Preprocessing Steps
1. Fetch latest markets from Manifold API.
2. Filter to unresolved binary markets with future close times.
3. Randomly sample 30 markets with fixed seed.
4. Store canonical fields (id, question, probability, close time, url).

### Train/Val/Test Splits
Not applicable; this is a paired evaluation on a fixed sample of markets.

## 4. Experiment Description

### Methodology
#### High-Level Approach
Generate two short future-news articles per market: baseline (no market probability) and market-informed (probability provided). Then evaluate outputs with an LLM judge for plausibility, coherence, and alignment with the provided probability.

#### Why This Method?
This directly tests the hypothesis that market signals improve narrative plausibility and calibration. Alternatives considered included human evaluation or historical market snapshots, but the current study prioritizes rapid, reproducible evaluation using an LLM judge.

### Implementation Details

#### Tools and Libraries
- openai 2.16.0
- pandas 3.0.0
- numpy 2.4.2
- scipy 1.17.0
- matplotlib 3.10.8
- seaborn 0.13.2

#### Algorithms/Models
- **Generation model**: `gpt-4.1`
- **Judge model**: `gpt-4.1`

#### Hyperparameters
| Parameter | Value | Selection Method |
|---|---|---|
| temperature | 0.7 (generation), 0.0 (judge) | standard for diversity / determinism |
| max_output_tokens | 700 | safe upper bound |

#### Training Procedure or Analysis Pipeline
1. Collect markets (Manifold API).
2. Generate baseline articles (no market prior).
3. Generate market-informed articles (probability prior included).
4. LLM judge scores each article.
5. Statistical comparison via paired t-tests; compute Cohen's d.

### Experimental Protocol

#### Reproducibility Information
- **Runs**: Single pass for generation and evaluation
- **Seeds**: Python random seed = 42 (market sampling)
- **Hardware**: NVIDIA GeForce RTX 3090 (not used for API calls), CPU-based execution
- **Execution time**: ~7 minutes end-to-end

#### Evaluation Metrics
- **Plausibility (1-5)**: How believable the narrative is given the question.
- **Coherence (1-5)**: Clarity and internal consistency.
- **Alignment (1-5)**: Consistency with market probability.
- **Probability error (0-1)**: Judge-estimated deviation from the market prior.
- **Hedging rate**: Simple rate of hedge tokens per 100 words.

### Raw Results

#### Tables
| Metric | Baseline mean | Market mean | p-value | Cohen's d | n |
|---|---:|---:|---:|---:|---:|
| plausibility | 4.367 | 5.000 | 4.28e-06 | 1.030 | 30 |
| coherence | 5.000 | 5.000 | NaN | 0.000 | 30 |
| alignment | 3.133 | 5.000 | 8.19e-09 | 1.459 | 30 |
| probability_error | 0.282 | 0.000 | 3.58e-08 | -1.354 | 30 |
| hedging_rate | 0.693 | 0.972 | 0.148 | 0.271 | 30 |
| word_count | 136.200 | 138.933 | 0.2 | 0.239 | 30 |

#### Visualizations
- Market probability distribution: `figures/market_probability_hist.png`
- Plausibility by condition: `figures/plausibility_boxplot.png`
- Alignment by condition: `figures/alignment_boxplot.png`
- Probability error by condition: `figures/probability_error_boxplot.png`

#### Output Locations
- Results JSON: `results/stats.json`
- Raw generations: `results/articles_baseline.jsonl`, `results/articles_market.jsonl`
- Judgments: `results/judgments.jsonl`
- Plots: `figures/`

## 5. Result Analysis

### Key Findings
1. Market-informed prompts significantly improved plausibility scores (p < 1e-5) with a large effect size (d ~ 1.0).
2. Alignment with market priors improved substantially (p < 1e-7), and probability error decreased to near-zero.
3. Coherence was already at ceiling (5.0) for both conditions, indicating no measurable gain.

### Hypothesis Testing Results
- **Supported**: Market-informed narratives are more plausible and better aligned with market priors.
- **Significance**: Plausibility and alignment differences are statistically significant; coherence is not.

### Comparison to Baselines
Market-informed prompts outperformed baseline on plausibility and alignment. Differences in length and hedging were small and not statistically significant.

### Surprises and Insights
- The judge frequently rated market-informed outputs at the maximum alignment score, suggesting the model strongly follows explicit probability priors.
- Coherence may be at ceiling for short (120-180 word) articles, limiting sensitivity.

### Error Analysis
- Baseline articles sometimes sounded overly definitive (e.g., "reports stable production") even when probabilities were near 0.5.
- Market-informed articles occasionally over-anchored on the probability (repeating it verbatim) without adding causal detail.

### Limitations
- No historical market snapshots; only current probabilities were used.
- LLM-as-judge introduces potential evaluation bias.
- Small sample size (n=29) and single-run generation.
- Some markets are niche; generalizability to mainstream news topics is uncertain.

## 6. Conclusions
Market probabilities materially improve plausibility and probabilistic alignment in LLM-generated future-news narratives in this small-scale study. This supports the hypothesis that prediction markets can serve as an effective prior for narrative generation, though stronger validation (larger samples, human evaluation, historical market snapshots) is needed.

### Implications
- **Practical**: Market-informed prompts could be used in a "news from the future" website to generate uncertainty-aware narratives.
- **Theoretical**: Highlights the value of probabilistic priors for narrative generation tasks.

### Confidence in Findings
Moderate. The effects are strong but rely on an LLM judge and a limited market sample.

## 7. Next Steps

### Immediate Follow-ups
1. Add human evaluation with blinded raters for plausibility and calibration.
2. Use historical market probability snapshots to avoid leakage and measure factual accuracy post-resolution.

### Alternative Approaches
- Test other market sources (Kalshi, Metaculus) for broader coverage.
- Compare with retrieval-augmented baselines (recent news summaries).

### Broader Extensions
- Integrate a live web interface that refreshes articles as probabilities change.
- Add entity tracking and factuality constraints to reduce hallucination.

### Open Questions
- How sensitive are narratives to small probability changes?
- Can we calibrate narrative tone to match market uncertainty more precisely?
