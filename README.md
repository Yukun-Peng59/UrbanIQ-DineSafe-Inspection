# UrbanIQ-DineSafe-Inspection

**Capstone Project – Risk-Based Inspection Prioritization using Toronto DineSafe Data**

## Overview
This repository contains the data, scripts, and documentation used in Humber College’s Capstone project for **BIA 5450**.
The goal is to build a risk-based model to identify high-risk restaurants using Toronto Public Health's DineSafe inspection dataset.

## Repository Structure
```
data/          → raw, cleaned, and metadata (dictionary)
scripts/       → ingestion and cleaning scripts
notebooks/     → exploratory and analytical notebooks
docs/          → flow diagrams, documentation, and figures
requirements.txt → Python dependencies
```

## Data Source
- **Origin**: City of Toronto Open Data Portal → https://open.toronto.ca/dataset/dinesafe/
- **Entity of Record**: Toronto Public Health (DineSafe Registry)
- **License**: Open Government Licence – Toronto
- **Data flow diagram**: see `/docs/Data_Flow_Diagram.png`

## How to Reproduce
```bash
pip install -r requirements.txt
python scripts/data_ingestion.py
python scripts/data_cleaning.py
```

Outputs will be saved under `data/cleaned/`.

## Team
UrbanIQ – Group 8  
- Chang Qin (PM)  
- Jiayu Zeng (Data Lead)  
- Yukun Peng (ML Lead)  
- Dax Oliver Filoteo (BI Dashboards)  
- Meixi Guo (Docs)
- Prashuna Sai Surya Vishwitha Domadula (QA)

