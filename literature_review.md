# Literature Review: News from the Future

## Review Scope

### Research Question
How can we combine LLMs with prediction-market signals to generate plausible news articles about future events, and how should such systems be evaluated?

### Inclusion Criteria
- LLM forecasting of future events or open-ended forecasting
- Datasets for event forecasting or temporal QA tied to real-world events
- Prediction markets used as evaluation or calibration signals
- Papers with methods, benchmarks, or data applicable to generating future-news narratives

### Exclusion Criteria
- Pure numeric time-series forecasting without event narratives
- Datasets without temporal anchoring or future-event focus
- Non-public or undocumented benchmarks

### Time Frame
2006–2026 (emphasis on 2021–2026)

### Sources
- arXiv
- ACL Anthology
- PMLR (ICML)
- NBER working papers
- HuggingFace datasets
- GitHub repositories

## Search Log

| Date | Query | Source | Results | Notes |
|------|-------|--------|---------|-------|
| 2026-02-01 | "LLM forecasting daily news oracle" | PMLR / arXiv | 1 | Daily Oracle paper (ICML 2025) |
| 2026-02-01 | "open-ended event forecasting dataset" | ACL Anthology | 1 | OpenForecast (COLING 2025) |
| 2026-02-01 | "open-ended forecasting from news OpenForesight" | arXiv / project site | 1 | OpenForecaster (arXiv 2026) |
| 2026-02-01 | "prediction market LLM calibration KalshiBench" | arXiv | 1 | KalshiBench (arXiv 2025) |
| 2026-02-01 | "ForecastQA event forecasting dataset" | ACL Anthology / project site | 1 | ForecastQA (ACL 2021) |
| 2026-02-01 | "SCTc-TE temporal event forecasting" | arXiv / GitHub | 1 | SCTc-TE + GDELT-ComplexEvent |
| 2026-02-01 | "prediction markets theory practice" | NBER | 2 | Wolfers & Zitzewitz papers |

Note: The paper-finder service was unavailable; manual search was used.

## Screening Results

| Paper | Title Screen | Abstract Screen | Full-Text | Notes |
|------|-------------|-----------------|-----------|-------|
| Dai et al. 2025 | Include | Include | Include | Daily Oracle benchmark; core to hypothesis |
| Wang et al. 2025 (OpenForecast) | Include | Include | Include | Large-scale open-ended dataset |
| Chandak et al. 2026 (OpenForecaster) | Include | Include | Include | Training LLM forecasters from news |
| Nel 2025 (KalshiBench) | Include | Include | Include | Prediction market calibration benchmark |
| Zhang et al. 2021 (ForecastQA) | Include | Include | Abstract | Early forecasting QA benchmark |
| Wang et al. 2023 (SCTc-TE) | Include | Include | Abstract | Temporal event forecasting formulation |
| Wolfers & Zitzewitz 2006 (PM theory) | Include | Include | Abstract | Foundational PM theory |
| Wolfers & Zitzewitz 2006 (PM prices) | Include | Include | Abstract | PM price-as-probability basis |

## Paper Summaries

### Paper 1: Are LLMs Prescient? A Continuous Evaluation using Daily News as the Oracle
- **Authors**: Hui Dai, Ryan Teehan, Mengye Ren
- **Year**: 2025
- **Source**: ICML 2025 (PMLR 267)
- **Key Contribution**: Daily Oracle, a continuously updated forecasting QA benchmark from daily news.
- **Methodology**:
  - Collects ~1.25M news articles (Common Crawl News + targeted sources).
  - LLM-generated TF and MC QA pairs with filtering rubric.
  - Evaluates closed-book, constrained open-book (BM25 RAG), and gold-article settings.
- **Datasets Used**: Daily Oracle (16,783 TF + 14,727 MC in the 2020–2024 analysis subset).
- **Baselines/Models**: GPT-4, GPT-3.5, Llama-3-8B, Mixtral, Claude-3.5, Qwen, Gemma.
- **Evaluation Metrics**: Accuracy, YoY accuracy decline, refusal rate.
- **Results**: Forecasting accuracy declines over time (average drop ~21.55% TF, ~11.33% MC). RAG improves accuracy but does not remove temporal degradation.
- **Code Available**: Yes (project page).
- **Relevance to Our Research**: Directly ties forecasting to daily news with a continuous, automatically generated benchmark.

### Paper 2: OpenForecast: A Large-Scale Open-Ended Event Forecasting Dataset
- **Authors**: Zhen Wang, Xi Zhou, Yating Yang, Bo Ma, Lei Wang, Rui Dong, Azmat Anwar
- **Year**: 2025
- **Source**: COLING 2025
- **Key Contribution**: Large-scale open-ended event forecasting dataset and tasks; LLM-based retrieval-augmented evaluation (LRAE).
- **Methodology**:
  - Collects complex events from Wikipedia and WCEP.
  - Uses extraction-then-complement LLM pipeline to build event timelines.
  - Defines open-ended tasks (STF/LTF/AQA) and closed-ended tasks (MCNC/MCAC/VQA).
- **Datasets Used**: OpenForecast (43,417 complex events; 473,155 atomic events, 1950–2024).
- **Baselines**: LLM-based evaluation with LRAE; comparisons with BEM/BertScore.
- **Evaluation Metrics**: Accuracy/F1 for tasks; LRAE for open-ended scoring.
- **Results**: LRAE provides higher consistency with human evaluation vs. baselines.
- **Code Available**: Yes (GitHub).
- **Relevance**: Provides open-ended event data suitable for generating future-news narratives.

### Paper 3: Scaling Open-Ended Reasoning To Predict the Future
- **Authors**: Nikhil Chandak, Shashwat Goel, Ameya Prabhu, Moritz Hardt, Jonas Geiping
- **Year**: 2026 (arXiv:2512.25070)
- **Source**: arXiv
- **Key Contribution**: OpenForesight dataset and RL training recipe to create OpenForecaster LLMs.
- **Methodology**:
  - Synthesizes open-ended forecasting questions from CommonCrawl News with filtering.
  - Uses retrieval from a static news corpus to avoid leakage.
  - Trains Qwen3 models with GRPO using a reward combining accuracy + adapted Brier score.
- **Datasets Used**: OpenForesight (~50k questions from ~250k articles); test set May–Aug 2025; FutureX benchmark.
- **Evaluation Metrics**: Accuracy, calibration, consistency, Brier-style reward.
- **Results**: OpenForecaster-8B competitive with larger proprietary models; improved calibration and consistency.
- **Code Available**: Yes (GitHub + HF).
- **Relevance**: Demonstrates end-to-end pipeline for open-ended future-event generation and evaluation.

### Paper 4: Do Large Language Models Know What They Don’t Know? (KalshiBench)
- **Authors**: Lukas Nel
- **Year**: 2025 (arXiv:2512.16030)
- **Source**: arXiv (NeurIPS 2024)
- **Key Contribution**: Prediction-market benchmark to evaluate LLM calibration on future events.
- **Methodology**:
  - Curates Kalshi prediction market questions; filters to post-cutoff resolutions.
  - Evaluates models on accuracy and calibration metrics.
- **Datasets Used**: KalshiBench (1,531 total; 300-question filtered sample).
- **Evaluation Metrics**: Accuracy, F1, Brier score, ECE, reliability diagrams, Brier Skill Score.
- **Results**: All models show overconfidence; only one model achieves positive Brier Skill Score.
- **Code Available**: Paper provides dataset; code link not specified in PDF.
- **Relevance**: Directly connects prediction markets with LLM uncertainty calibration.

### Paper 5: ForecastQA: A Question Answering Challenge for Event Forecasting with Temporal Text Data
- **Authors**: Jingqing Zhang, Yao Zhao, Mohammad Saleh, Peter J. Liu, Yang Liu
- **Year**: 2021
- **Source**: ACL 2021
- **Key Contribution**: Early forecasting QA dataset with temporal constraints and MC/yes-no formats.
- **Methodology**: Constructs forecasting questions grounded in temporal text; compares neural baselines.
- **Datasets Used**: ForecastQA (train/dev/test public splits).
- **Evaluation Metrics**: Accuracy.
- **Results**: Human performance substantially exceeds baseline models; dataset remains challenging.
- **Code Available**: Dataset available via project site.
- **Relevance**: Provides baseline QA format for event forecasting with temporal grounding.

### Paper 6: SCTc-TE: A Comprehensive Formulation and Benchmark for Temporal Event Forecasting
- **Authors**: Yunchong Wang, Shuo Wang, Jialong Han, Haifeng Wang, Ming Gao, Xiangnan He, Yongdong Zhang
- **Year**: 2023 (arXiv:2312.01052)
- **Source**: arXiv
- **Key Contribution**: Formalizes SCTc-TE and introduces MidEast-TE and GDELT-TE datasets plus LoGo model.
- **Methodology**: Builds structured complex event timelines and predicts future temporal events using local/global context graphs.
- **Datasets Used**: MidEast-TE, GDELT-TE.
- **Evaluation Metrics**: Event prediction accuracy; graph-based model comparisons.
- **Results**: LoGo improves over baselines by leveraging local + global contexts.
- **Code Available**: Yes (GDELT-ComplexEvent repo).
- **Relevance**: Provides structured event forecasting data and baseline model.

### Paper 7: Prediction Markets in Theory and Practice
- **Authors**: Justin Wolfers, Eric Zitzewitz
- **Year**: 2006
- **Source**: NBER Working Paper 12083
- **Key Contribution**: Summarizes theory and empirical results showing prediction markets can aggregate dispersed information effectively.
- **Relevance**: Provides grounding for using market prices as probabilistic signals.

### Paper 8: Interpreting Prediction Market Prices as Probabilities
- **Authors**: Justin Wolfers, Eric Zitzewitz
- **Year**: 2006
- **Source**: NBER Working Paper 12200
- **Key Contribution**: Provides conditions under which prediction market prices approximate mean beliefs of traders.
- **Relevance**: Supports using prediction market prices as probabilistic priors for LLM-generated futures.

## Common Methodologies
- **LLM-based question generation**: Daily Oracle, OpenForesight, OpenForecast use LLMs to extract events and build questions.
- **Retrieval-augmented forecasting**: BM25 or embedding retrieval to add recent news context.
- **Open-ended evaluation**: LLM-as-judge or retrieval-augmented scoring (LRAE).
- **Calibration-focused evaluation**: Brier score, ECE, and reliability diagrams (KalshiBench).

## Standard Baselines
- **Closed-book LLM forecasting** without retrieval
- **BM25 RAG** for constrained open-book forecasting
- **Graph-based models** (LoGo) for structured event prediction
- **Text similarity metrics** (BEM/BertScore) for open-ended scoring

## Evaluation Metrics
- Accuracy (TF/MC/MCNC/MCAC)
- F1 (open-ended tasks where applicable)
- Brier score / Brier Skill Score
- Expected Calibration Error (ECE)
- Reliability diagrams / refusal rate

## Datasets in the Literature
- Daily Oracle (continuous news-based QA)
- OpenForesight (open-ended forecasting from news)
- OpenForecast (open-ended event forecasting from Wikipedia/WCEP)
- ForecastQA (temporal forecasting QA)
- SCTc-TE (MidEast-TE, GDELT-TE)
- KalshiBench (prediction market questions)

## Gaps and Opportunities
- **Narrative generation**: Current benchmarks focus on QA or short answers; few evaluate full news-style narratives.
- **Market integration**: Prediction market probabilities are rarely used to guide or calibrate LLM-generated content.
- **Temporal leakage control**: Stronger tooling is needed for preventing leakage when using live retrieval.
- **Evaluation**: Open-ended evaluation metrics remain noisy; human-aligned metrics for narrative plausibility are limited.

## Recommendations for Our Experiment
- **Recommended datasets**:
  - ForecastQA (lightweight QA baseline)
  - Daily Oracle (continuous news-based evaluation)
  - OpenForesight (open-ended training data)
  - OpenForecast (complex event sequences)
- **Recommended baselines**:
  - Closed-book LLM + RAG variants (BM25 + embedding retrieval)
  - LoGo or other structured event baselines for comparison
- **Recommended metrics**:
  - Accuracy for QA tasks; Brier/ECE for calibration
  - LLM-as-judge or LRAE for open-ended responses
- **Methodological considerations**:
  - Enforce strict temporal cutoffs to prevent leakage
  - Use prediction market probabilities for calibration or as priors in generation
  - Evaluate narrative plausibility separately from factual correctness
