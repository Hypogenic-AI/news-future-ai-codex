# Cloned Repositories

## Repo 1: openforecaster/scaling-forecasting-training
- URL: https://github.com/openforecaster/scaling-forecasting-training
- Purpose: End-to-end pipeline for open-ended forecasting (question generation, retrieval, RL training, evaluation) used in OpenForesight/OpenForecaster.
- Location: code/openforecaster_scaling_forecasting/
- Key files/directories:
  - qgen/: generate forecasting questions from news with filtering/leakage checks
  - libraries/verl/: RL training utilities and examples
  - custom_eval_scripts/: evaluation scripts for free-form and binary questions
  - local_judge/: LLM-as-judge answer matching
- Notes: Requires separate environment for VERL/RL training; dataset is on HuggingFace (OpenForesight).

## Repo 2: miaomiao1215/Openforecast
- URL: https://github.com/miaomiao1215/Openforecast
- Purpose: Code and data access for OpenForecast dataset (open-ended event forecasting).
- Location: code/openforecast/
- Key files/directories:
  - README.md with Google Drive download for dataset
- Notes: Dataset download link is provided in README; no code usage details beyond data download.

## Repo 3: yecchen/GDELT-ComplexEvent
- URL: https://github.com/yecchen/GDELT-ComplexEvent
- Purpose: Code + data for SCTc-TE benchmark, includes MidEast-TE and GDELT-TE datasets and LoGo model.
- Location: code/gdelt-complexevent/
- Key files/directories:
  - data/ (MIDEAST_CE.zip, GDELT_CE.zip)
  - dataset_construction/: pipeline for building datasets
  - generate_graphs_ce.py: graph construction for training
  - train_logo_early.py / train_logo_late.py: LoGo training scripts
- Notes: Requires PyTorch + DGL; dataset zips must be unzipped in repo.
