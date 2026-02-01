# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT
committed to git due to size. Follow the download instructions below.

## Dataset 1: ForecastQA

### Overview
- **Source**: https://inklab.usc.edu/ForecastQA/
- **Size**: Train 8,210 (4,737 yes/no + 3,473 MC), Dev 1,090, Test 1,092
- **Format**: JSON
- **Task**: Event forecasting QA (yes/no and multiple-choice)
- **Splits**: train/dev/test (public)
- **Location**: datasets/forecastqa/

### Download Instructions
This dataset is already downloaded locally in `datasets/forecastqa/`.
To re-download:
```bash
wget https://inklab.usc.edu/ForecastQA/forecastQA.zip -O datasets/forecastqa.zip
unzip datasets/forecastqa.zip -d datasets/forecastqa
```

### Loading the Dataset
```python
import json

with open("datasets/forecastqa/forecastQA_train_public.json") as f:
    data = json.load(f)
print(len(data["yesno_questions"]), len(data["multichoice_questions"]))
```

### Sample Data
See `datasets/forecastqa/samples.json`.

### Notes
- JSON is a dict with `yesno_questions` and `multichoice_questions` lists.

---

## Dataset 2: Daily Oracle (from Daily News)

### Overview
- **Source**: https://agenticlearning.ai/daily-oracle
- **Size**: 16,783 TF + 14,727 MC questions (Jan 2020–Dec 2024 subset used in paper)
- **Format**: QA pairs generated from daily news
- **Task**: Temporal forecasting QA

### Download Instructions
Refer to the project page for data access instructions:
- https://agenticlearning.ai/daily-oracle

### Notes
- Dataset is continuously updated; local download not attempted due to size and updates.

---

## Dataset 3: OpenForesight (OpenForecaster)

### Overview
- **Source**: https://huggingface.co/datasets/nikhilchandak/OpenForesight
- **Size**: ~50k open-ended forecasting questions (paper)
- **Format**: HuggingFace dataset
- **Task**: Open-ended forecasting

### Download Instructions (HuggingFace)
```python
from datasets import load_dataset

# Requires: pip install datasets

dataset = load_dataset("nikhilchandak/OpenForesight")
dataset.save_to_disk("datasets/openforesight")
```

### Notes
- Large dataset; not downloaded locally in this phase.

---

## Dataset 4: OpenForecast

### Overview
- **Source**: https://github.com/miaomiao1215/Openforecast
- **Size**: 43,417 complex events; 473,155 atomic events (paper)
- **Format**: Provided via Google Drive link in repo
- **Task**: Open-ended event forecasting (STF/LTF/AQA + closed-ended variants)

### Download Instructions
Follow the Google Drive link in the repo README:
- `code/openforecast/README.md`

---

## Dataset 5: SCTc-TE (MidEast-TE, GDELT-TE)

### Overview
- **Source**: https://github.com/yecchen/GDELT-ComplexEvent
- **Format**: Zipped data files in repo (`data/`)
- **Task**: Temporal event forecasting with structured complex events

### Download Instructions
In the repo, unzip the provided data:
```bash
cd code/gdelt-complexevent
unzip data/MIDEAST_CE.zip -d data
unzip data/GDELT_CE.zip -d data
```

### Notes
- Data is packaged inside the repo and not copied into `datasets/` to avoid duplication.

