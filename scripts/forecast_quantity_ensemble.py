import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta
import duckdb
import os
import warnings

print("🐍 Script is starting...")

try:
    print("Step 1: Connecting to DuckDB")
    DB_PATH = os.path.abspath("dbt.duckdb")
    print("🔌 Trying DuckDB connection...")
    try:
        con = duckdb.connect(DB_PATH)
        print("✅ Connection worked")
    except Exception as e:
        print("❌ DuckDB connection failed:")
        print(e)

    print("Step 2: Running query")
    QUERY = '''
        SELECT *
        FROM fct_quantity_by_customer
        ORDER BY month, country, customer_id
    '''
    print("Query defined...")
    df = con.execute(QUERY).fetchdf()
    print("Query executed...")
    print(f"✅ Query returned {len(df)} rows.")
    print(df.head())

    print("Step 3: Parsing dates")
    df['month'] = pd.to_datetime(df['month'])

    print("Step 4: Cleaning quantity")
    df['total_quantity'] = pd.to_numeric(df['total_quantity'], errors='coerce').fillna(0)

    print("Step 5: Basic data checks")
    print(f"Loaded rows: {len(df)}")
    print(df.head())

    print("Step 6: Grouping top customers")
    top_customers = (
        df.groupby(['customer_id', 'country'])['total_quantity']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    print(top_customers)

    from datetime import timedelta

    results = []
    FORECAST_MONTHS = 12
    OUTPUT_PATH = "data/forecast_quantity_ensemble.csv"

    for _, row in top_customers.iterrows():
        print(f"📦 Forecasting for customer {row['customer_id']} in {row['country']}")
        cust_id, country = row['customer_id'], row['country']
        sub = df[(df['customer_id'] == cust_id) & (df['country'] == country)].copy()
        sub = sub.sort_values('month')

        full_months = pd.date_range(start=sub['month'].min(), end=sub['month'].max(), freq='MS')
        sub = sub.set_index('month').reindex(full_months).fillna(0).rename_axis('month').reset_index()
        sub['customer_id'] = str(int(float(cust_id)))
        sub['country'] = country

        # ARIMA
        arima_model = ARIMA(sub['total_quantity'], order=(1, 1, 1)).fit()
        arima_forecast = arima_model.forecast(steps=FORECAST_MONTHS)

        # Regression
        sub['month_num'] = np.arange(len(sub))
        from sklearn.linear_model import LinearRegression

        reg_model = LinearRegression().fit(sub[['month_num']], sub['total_quantity'])
        future_months = pd.date_range(sub['month'].max() + pd.DateOffset(months=1), periods=FORECAST_MONTHS, freq='MS')
        future_df = pd.DataFrame({
            'month': future_months,
            'month_num': np.arange(len(sub), len(sub) + FORECAST_MONTHS)
        })
        reg_forecast = reg_model.predict(future_df[['month_num']])

        # Ensemble
        ensemble = (arima_forecast.values + reg_forecast) / 2

        for i in range(FORECAST_MONTHS):
            results.append({
                'customer_id': str(int(float(cust_id))),
                'country': country,
                'month': future_months[i],
                'forecast_quantity': ensemble[i],
                'arima': arima_forecast.values[i],
                'regression': reg_forecast[i]
            })
        print(f"✅ Finished forecasts for {cust_id} ({country})")

    # Export
    forecast_df = pd.DataFrame(results)
    forecast_df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Forecast saved to {OUTPUT_PATH}")


except Exception as e:
    print("❌ Script failed with error:")
    print(e)

print("🏁 Script finished!")
