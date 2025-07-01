import pandas as pd
import matplotlib.pyplot as plt

# Load forecast data
df = pd.read_csv("data/forecast_quantity_ensemble.csv")
df['month'] = pd.to_datetime(df['month'])

# Identify top 2 customers
top_customers = (
    df.groupby(['customer_id', 'country'])['forecast_quantity']
    .sum()
    .nlargest(2)
    .reset_index()
)

# Plot ensemble, ARIMA, and Regression forecasts
for _, row in top_customers.iterrows():
    cust_id = row['customer_id']
    country = row['country']
    sub = df[(df['customer_id'] == cust_id) & (df['country'] == country)]

    plt.figure(figsize=(10, 5))
    plt.plot(sub['month'], sub['forecast_quantity'], label='Ensemble Forecast', marker='o')
    plt.plot(sub['month'], sub['arima'], label='ARIMA', linestyle='--')
    plt.plot(sub['month'], sub['regression'], label='Regression', linestyle=':')
    plt.title(f"Forecast for Customer {cust_id} in {country}")
    plt.xlabel("Month")
    plt.ylabel("Forecasted Quantity")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
