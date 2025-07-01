Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


#### Draft README for dbt project that is co-located with EXAMPLE
# 📦 Sales Forecasting Demo Project

## 🧾 Summary
This project demonstrates a complete forecasting pipeline using Python, dbt, and DuckDB. It prepares and models retail sales data, generates customer-level forecasts, validates model accuracy, and visualizes trends in Python and Tableau Public.

---

## 📁 Project Structure
```
├── models/                          # dbt models (staging, marts, forecasts)
├── scripts/                         # Python scripts for ETL, forecasting, and plotting
├── data/                            # Input and output data files (CSV)
├── dbt_project.yml                  # dbt project configuration
├── profiles/                        # dbt profile for DuckDB (if applicable)
├── .gitignore                       # Ignore compiled Python/dbt/venv artifacts
└── README.md                        # Project documentation
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

## 📊 Tableau Dashboard
The final output includes a two-tabbed dashboard:

1. **Country Overview**: Trend lines of total units and revenue per country by month
2. **Customer Forecast**: Forecast trend (ARIMA, regression, ensemble) for individual customers

> [🔗 Tableau Public Link](https://public.tableau.com/app/profile/YOUR_PROFILE)

---

## 🧰 Tech Stack
- **Python**: pandas, matplotlib, statsmodels, scikit-learn
- **dbt**: data modeling & transformations
- **DuckDB**: local analytical database
- **Tableau Public**: dashboard visualization

---

## ✅ Setup Instructions
1. Clone the repo and create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Run scripts in this order:
```bash
python scripts/load_csvs_to_duckdb.py
dbt build
python scripts/forecast_quantity_ensemble.py
python scripts/validate_forecast_accuracy.py
python scripts/export_marts_to_csv.py
```

3. Open `data/*.csv` in Tableau Public and build dashboards.

---

## 🙋‍♀️ Author
Noelle Diederich  
[LinkedIn Profile](https://www.linkedin.com/in/YOUR-LINK)  
[Tableau Public](https://public.tableau.com/app/profile/YOUR_PROFILE)

