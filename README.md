# 🧠 dbt Forecasting Demo with Python + Tableau

This project demonstrates an end-to-end forecasting pipeline combining **dbt**, **Python**, and **Tableau**. It showcases demand forecasting using customer sales data and produces both customer-level and country-level forecasts, visualized in Tableau and Matplotlib.

## 📊 Project Overview

- **Goal**: Forecast product sales quantity and revenue by customer and country
- **Dataset**: [UCI Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
- **Tools Used**:
  - `dbt` for data modeling and transformation
  - `DuckDB` as the local database
  - `Python` for forecasting, validation, and visualization
  - `Tableau` for interactive dashboards
  - `scikit-learn`, `statsmodels` for ML models (ARIMA + linear regression)

## 🔧 Project Structure
```
dbt_forecasting_demo/
│
├── data/                            # CSV input + output files
  ├── forecast_quantity_ensemble.csv
  ├── fct_monthly_sales.csv
│  
├── models/                          # dbt models (staging, marts, audits)
  ├── marts/
  └── forecasting/
  ├── fct_monthly_sales.sql
  ├── fct_quantity_by_customer_sql
│ 
├── scripts/                        # Python scripts for modeling & charts
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
├── dbt_project.yml                 # dbt project config
└── README.md                       # Project documentation
```

---

## 🔄 Workflow Overview

### Step 1: Data Load & Modeling
- `scripts/load_csvs_to_duckdb.py`: Loads raw retail CSV data into DuckDB
- `dbt build`: Runs models to create marts like:
  - `fct_quantity_by_customer`
  - `fcst_monthly_sales`

### Step 2: Forecasting
- `scripts/forecast_quantity_ensemble.py`: Creates forecasts using ARIMA & Linear Regression
- `scripts/validate_forecast_accuracy.py`: Merges actuals and forecasts, computes MAE

### Step 3: Export & Visualize
- `scripts/export_marts_to_csv.py`: Writes dbt mart outputs to CSV for Tableau
- `scripts/visualize_fct_monthly_sales.py`: Generates country-level forecast trends
- `scripts/forecast_customer_charts.py`: Plots top customer forecasts

---

## 📈 Tableau Dashboard

Check out the published dashboard:
🔗 [Sales Forecast Dashboard on Tableau Public](https://public.tableau.com/app/profile/noelle.diederich/viz/tableau_dbt_fcst_demo1/SalesForecastDashboard)

Includes:
- **Country Overview**: Units and Revenue trends by country
- **Customer View**: Forecasted quantity per customer using ARIMA & Regression
---

## 🧰 Tech Stack
- **Python**: pandas, matplotlib, statsmodels, scikit-learn
- **dbt**: data modeling & transformations
- **DuckDB**: local analytical database
- **Tableau Public**: dashboard visualization

---

## ✅ Setup Instructions
1. Clone the repo:
```bash
   git clone https://github.com/nomadic-ore/dbt-forecasting-demo.git
   cd dbt-forecasting-demo
```

2. Create & Activate Virtual Environment, including Dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
# OR
.venv\Scripts\activate     # For Windows
```
```bash
pip install -r requirements.txt
```

3. Initialize dbt & Run Models.
```bash
dbt deps      # if using any packages
dbt build     # runs staging and mart models into DuckDB
```
4. Run Python Forecasting & Visualization (/output/forecast_charts, /output/country_trends).
```bash
python scripts/forecast_quantity_ensemble.py
python scripts/forecast_customer_charts.py
python scripts/visualize_fct_monthly_sales.py
```
5.  Open Tableau and point to the CSV files in the /data/folder (fct_monthly_sales.csv, forecast_quantity_ensemble.csv)
---

## 🙋‍♀️ Author
Noelle Diederich  
[LinkedIn Profile](https://www.linkedin.com/in/noelle-diederich)  
[Tableau Public](https://public.tableau.com/app/profile/noelle.diederich)

