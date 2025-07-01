# 🧠 dbt Forecasting Demo with Python + Tableau

This project demonstrates an end-to-end forecasting pipeline combining **dbt**, **Python**, and **Tableau**. It showcases demand forecasting using customer sales data and produces both customer-level and country-level forecasts, visualized in Tableau and Matplotlib.  

This project emphasizes learning and integration over polish. The Tableau dashboard is included to illustrate how outputs from dbt and Python can be consumed by business intelligence tools. Enhancements to interactivity and design are possible, but were not the primary focus in this iteration.

## 📊 Project Overview

- **Goal**: Forecast product sales quantity and revenue by customer and country
- **Dataset**: [UCI Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
- **Tools Used**:
  - `dbt` for data modeling and transformation
  - `DuckDB` as the local database
  - `Python` for forecasting, validation, and visualization
  - `Tableau` for interactive dashboards
  - `scikit-learn`, `statsmodels` for ML models (ARIMA + linear regression)

---

## 🔧 Project Structure

```
dbt_forecasting_demo/
│
├── data/                            # CSV input + output files
  ├── forecast_quantity_ensemble.csv
  └── fct_monthly_sales.csv
│  
├── models/                          # dbt models (staging, marts, audits)
  ├── marts/
  └── forecasting/
  ├── fct_monthly_sales.sql
  ├── fct_quantity_by_customer_sql
│ 
├── scripts/                        # Python scripts
│ ├── forecast_quantity_ensemble.py
│ ├── forecast_customer_charts.py
│ ├── visualize_fct_monthly_sales.py
│ ├── validate_forecast_accuracy.py
│
├── output/                         # Auto-generated forecast charts
│ ├── forecast_charts/
│ └── country_trends/
│
├── tableau_dbt_fcst_demo1.twb      # Tableau workbook file
├── dbt.duckdb                      # DuckDB database file
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git exclusions
├── LICENSE.md                      # MIT License
├── dbt_project.yml                 # dbt project config
└── README.md                       # Project documentation
```

---


---

## 🔄 Workflow Overview

### Step 1: Load & Model Data
- Run `scripts/load_csvs_to_duckdb.py` to ingest the dataset into DuckDB
- Run dbt models:
  ```bash
  dbt build

### Step 2: Forecasting
- Run ARIMA + Linear Regression ensemble:
  ```bash
  python scripts/forecast_quantity_ensemble.py
- Optional: Validate accuracy vs. actuals
  ```bash
  python scripts/validate_forecast_accuracy.py

### Step 3: Export Visuals
- Country-level plots::
  ```bash
  python scripts/visualize_fct_monthly_sales.py
- Top customer forecasts
  ```bash
  python scripts/forecast_customer_charts.py

---

## 📈 Tableau Dashboard

Check out the published dashboard:
🔗 [Sales Forecast Dashboard on Tableau Public](https://public.tableau.com/app/profile/noelle.diederich/viz/tableau_dbt_fcst_demo1/SalesForecastDashboard)

Includes:
- **Country Overview**: Units and Revenue trends by country
- **Customer View**: Forecasted quantity per customer using ARIMA & Regression
---


## ✅ Setup Instructions
1. Clone & Set Up Environment
```bash
git clone https://github.com/your-username/dbt_forecasting_demo.git
cd dbt_forecasting_demo
python -m venv .venv
.venv\Scripts\activate  # (or use source .venv/bin/activate for Mac/Linux)
pip install -r requirements.txt
```
2. Run dbt Models
```bash
dbt build
```

3. Run Forecast & Visualizations
```bash
python scripts/forecast_quantity_ensemble.py
python scripts/forecast_customer_charts.py
python scripts/visualize_fct_monthly_sales.py
```
5.  Open Tableau
- Open tableau_dbt_fcst_demo1.twb
- Point to data/fct_monthly_sales.csv and forecast_quantity_ensemble.csv
---

## 🔐 License
- Licensed under the MIT License

---

## 🙋‍♀️ Author
Noelle Diederich  
[LinkedIn Profile](https://www.linkedin.com/in/noelle-diederich)  
[Tableau Public](https://public.tableau.com/app/profile/noelle.diederich)

