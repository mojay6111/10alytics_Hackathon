# 10Alytics Hackathon 2025 🏆
### AI-Powered Fiscal Intelligence for African Economies

---

## 📌 Problem Statement

Across many developing economies — including Nigeria and other African countries — fiscal, economic, and demographic data are under-utilized in policymaking. This project uses **AI, data science, and analytical modelling** to transform fragmented macroeconomic and fiscal indicators into meaningful, actionable intelligence aligned with the **UN Sustainable Development Goals (SDGs)**.

---

## 🎯 Objectives

| # | Research Question |
|---|---|
| 1 | What are the **fiscal stability trends** across African countries? |
| 2 | How do macroeconomic indicators **correlate** with development outcomes? |
| 3 | Which country-years represent **high fiscal risk anomalies**? |
| 4 | Can we **predict and forecast** fiscal indicators to support policy decisions? |

---

## 📁 Project Structure

```
10alytics_Hackathon/
│
├── data/
│   ├── raw/                          # Original unmodified source data
│   │   └── 10Alytics_Fiscal_Data.csv
│   └── processed/                    # Cleaned & transformed data
│       └── 10Alytics_Fiscal_Panel_Data.csv
│
├── notebooks/
│   ├── 01_02_03_data_eda_anomaly.ipynb   # Data loading, EDA, anomaly detection
│   └── 04_predictive_modeling.ipynb      # Phase 4: ML forecasting & policy
│
├── src/                              # Reusable Python modules
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── visualization.py
│   └── modeling.py
│
├── outputs/
│   ├── figures/                      # All generated plots
│   │   ├── correlation_heatmap.png
│   │   ├── fiscal_stability_trends.png
│   │   └── anomaly_score_distribution.png
│   └── reports/                      # Final submission documents
│
├── models/                           # Saved trained model files
│   └── isolation_forest_v1.pkl
│
├── requirements.txt
├── setup_project.sh
└── README.md
```

---

## 📊 Dataset Overview

| File | Description | Rows | Format |
|------|-------------|------|--------|
| `10Alytics_Fiscal_Data.csv` | Raw long-format fiscal & macro indicators | ~30,000+ | Long (melted) |
| `10Alytics_Fiscal_Panel_Data.csv` | Cleaned wide-format panel data | Pivoted by Country-Year | Wide (panel) |

### Key Indicators Covered
- Budget Deficit / Surplus
- Government Debt
- GDP Growth Rate & GDP per Capita
- Inflation Rate & Consumer Price Index (CPI)
- Revenue & Expenditure
- Tax Revenue & VAT
- Capital Expenditure & Health Expenditure
- Unemployment Rate
- Trade Data & Population Metrics

### Countries of Focus
`Nigeria` · `South Africa` · `Ghana` · `Egypt` · `Kenya`

---

## 🔬 Methodology

### Phase 1 — Data Loading & Cleaning
- Loaded raw CSV into pandas DataFrame
- Converted `Time` to datetime, `Amount` to numeric
- Standardized indicator names (lowercase, stripped whitespace, unified variants)
- Imputed missing `Currency` values by country-mode
- Dropped rows with missing `Time`, `Amount`, or `Unit`

### Phase 2 — Exploratory Data Analysis (EDA)
- Fiscal Stability Trends: Budget Balance & Government Debt per country (1990–present)
- Inflation Rate trends across top 5 countries
- Pearson correlation heatmap across 10 core macroeconomic variables

### Phase 3 — Anomaly & Risk Detection
- Model: **Isolation Forest** (`contamination=0.05`, `n_estimators=100`)
- Features: Budget Deficit/Surplus, Government Debt, Revenue, Expenditure, GDP Growth Rate
- **Key Finding:** Nigeria 2020 & 2023 are the highest fiscal risk anomalies, driven by extreme deficit, debt, and negative GDP growth

### Phase 4 — Predictive Modeling & Policy (ML)
- **GDP Growth Rate Forecasting** using Prophet time-series model
- **Fiscal Risk Classification** using XGBoost (country-year risk scoring)
- **Country Clustering** using K-Means for policy segmentation

---

## 🚀 Getting Started

### 1. Clone / Navigate to the project
```bash
cd "/mnt/d/DS PROJECTS/10alytics_Hackathon"
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the setup script (first time only)
```bash
bash setup_project.sh
```

### 5. Launch Jupyter
```bash
jupyter notebook
```

---

## 📈 Key Findings

- 🔴 **Nigeria** shows the most severe fiscal anomalies (2020, 2023) with extreme deficits and negative GDP growth
- 📉 Most African countries in the dataset ran **chronic deficits** post-1990
- 🔗 Strong positive correlation between **Government Debt** and **Expenditure**
- 💹 **Inflation volatility** is highest in Nigeria and Ghana, directly impacting SDG 1 & SDG 2

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.10+ |
| Data Wrangling | pandas, numpy |
| Visualization | matplotlib, seaborn, plotly |
| Machine Learning | scikit-learn, xgboost, lightgbm |
| Time Series | Prophet, statsmodels |
| Environment | Jupyter Notebook, conda/venv |

---

## 👤 Author

**cap_mojay** — 10Alytics Hackathon 2025 Participant

---

## 📄 License

This project was developed for the **10Alytics Hackathon 2025** competition. Data belongs to the competition organizers.
