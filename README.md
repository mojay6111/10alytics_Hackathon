# 🌍 African Fiscal Intelligence Platform
### 10Alytics Hackathon 2025

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://10alytics-fiscal-intelligence.streamlit.app)
[![GitHub](https://img.shields.io/badge/GitHub-mojay6111-181717?style=flat&logo=github)](https://github.com/mojay6111/10alytics_Hackathon)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

> **AI-powered analysis of macroeconomic and fiscal indicators across 14 African economies — transforming fragmented data into actionable policy intelligence aligned with the UN SDGs.**

---

## 🎯 Problem Statement

Across many developing economies — including Nigeria and other African countries — fiscal, economic, and demographic data are under-utilized in policymaking. Governments collect large volumes of information on budgets, GDP, trade, taxation, health and population dynamics, yet these datasets are often fragmented, not integrated, and rarely translated into actionable insights.

This project uses **AI, data science, and analytical modelling** to transform fragmented macroeconomic and fiscal indicators into meaningful intelligence aligned with the **UN Sustainable Development Goals (SDGs)**.

---

## 🚀 Live Demo

👉 **[Launch the App](https://10alytics-fiscal-intelligence.streamlit.app)**

| Page | Description |
|------|-------------|
| 🏠 Home | Platform overview and key statistics |
| 📈 GDP Forecasts | 5-year Prophet forecasts with confidence intervals |
| ⚠️ Fiscal Risk Scorer | Live AI-powered risk scoring tool |
| 🗺️ Country Clusters | Interactive Africa map + radar charts |
| 📋 Policy Advisor | SDG-aligned policy recommendations per country |

---

## 📁 Project Structure

```
10alytics_Hackathon/
│
├── data/
│   ├── raw/
│   │   └── 10Alytics_Fiscal_Data.csv
│   └── processed/
│       ├── 10Alytics_Fiscal_Panel_Data.csv
│       └── corrected_country_clusters.csv
│
├── notebooks/
│   ├── 01_02_03_data_eda_anomaly.ipynb
│   ├── 04_predictive_modeling.ipynb
│   └── 05_normalized_clustering.ipynb
│
├── streamlit_app/
│   ├── app.py
│   ├── requirements.txt
│   └── pages/
│       ├── 01_GDP_Forecasts.py
│       ├── 02_Fiscal_Risk_Scorer.py
│       ├── 03_Country_Clusters.py
│       └── 04_Policy_Advisor.py
│
├── models/
│   ├── xgboost_fiscal_risk_v1.pkl
│   └── scaler_v1.pkl
│
├── outputs/figures/
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

| File | Description | Rows |
|------|-------------|------|
| `10Alytics_Fiscal_Data.csv` | Raw long-format fiscal indicators | ~30,000+ |
| `10Alytics_Fiscal_Panel_Data.csv` | Cleaned wide-format panel data | 6,159 |
| `corrected_country_clusters.csv` | Z-score normalized cluster assignments | 10 |

**14 Countries:** Algeria · Angola · Botswana · Egypt · Ethiopia · Ghana · Ivory Coast · Kenya · Nigeria · Rwanda · Senegal · South Africa · Tanzania · Togo

**65 Years of Data:** 1960 – 2025 · **20+ Indicators**

---

## 🔬 Methodology

| Phase | Description |
|-------|-------------|
| 1 | Data loading, type conversion, indicator standardization, panel pivot |
| 2 | EDA — fiscal trends, inflation analysis, Pearson correlation heatmap |
| 3 | Anomaly detection — Isolation Forest (Nigeria 2020/2023 flagged) |
| 4 | Predictive modelling — Prophet forecasts, XGBoost risk classifier, K-Means clusters |
| 5 | Currency-normalized clustering — Z-score fix for NGN/USD scale distortion |

---

## 📈 Key Findings

| Finding | Detail |
|---------|--------|
| 🔴 Nigeria | Most fiscally stressed — chronic deficits, high inflation |
| 📉 South Africa | Trending toward negative GDP growth by 2027–28 |
| 🟢 Kenya | Strongest growth outlook (~5.7–5.9% through 2029) |
| 💹 Ghana | Steady recovery post-debt restructuring (~4.1–4.3%) |
| ⚠️ Currency Bias | Raw nominal clustering misclassified Nigeria as Stable due to NGN scale |

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.11 |
| Data Wrangling | pandas, numpy |
| Visualisation | matplotlib, seaborn, plotly |
| Machine Learning | scikit-learn, xgboost |
| Time Series | Prophet |
| Web App | Streamlit |

---

## ⚙️ Run Locally

```bash
git clone https://github.com/mojay6111/10alytics_Hackathon.git
cd 10alytics_Hackathon
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

---

## 🌐 Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **New app** → select `mojay6111/10alytics_Hackathon`
3. Set **Main file path** → `streamlit_app/app.py`
4. Click **Deploy** 🚀

---

## 👤 Author

**mojay6111** — 10Alytics Hackathon 2025

[![GitHub](https://img.shields.io/badge/GitHub-mojay6111-181717?style=flat&logo=github)](https://github.com/mojay6111/10alytics_Hackathon)

---

<p align="center">Built with ❤️ for African fiscal intelligence · 10Alytics Hackathon 2025</p>
