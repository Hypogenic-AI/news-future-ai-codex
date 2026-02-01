# News from the Future (LLM + Prediction Markets)

This project tests whether adding prediction-market probabilities to LLM prompts produces more plausible and better-calibrated future-news narratives than baseline prompts without market signals.

## Key Findings
- Market-informed prompts significantly improved plausibility and alignment scores.
- Probability error dropped substantially when market priors were provided.
- Coherence was already at ceiling for both conditions in short articles.

## Reproduce
```bash
# Activate environment
source .venv/bin/activate

# Collect markets and run pipeline
python src/collect_markets.py
python src/eda_markets.py
python src/generate_articles.py
python src/judge_articles.py
python src/analyze_results.py
```

## Website Demo
```bash
# Serve the demo site from the workspace root
python -m http.server 8000
# Then open: http://localhost:8000/site/
```

## File Structure
- `src/` scripts for data collection, generation, judging, analysis
- `results/` raw outputs and statistics
- `figures/` plots
- `site/` static demo website
- `REPORT.md` full report

## Full Report
See `REPORT.md` for methodology, results, and analysis.
