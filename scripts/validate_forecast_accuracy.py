import pandas as pd
import duckdb
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("🔍 Starting forecast accuracy validation...")

# === Load forecasted data from CSV ===
forecast_df = pd.read_csv("data/forecast_quantity_ensemble.csv")
forecast_df["month"] = pd.to_datetime(forecast_df["month"]).dt.to_period("M")
forecast_df["customer_id"] = forecast_df["customer_id"].astype(float).astype(int).astype(str)
forecast_df["country"] = forecast_df["country"].astype(str)

# === Load actuals from DuckDB ===
con = duckdb.connect("dbt.duckdb")
actuals_df = con.execute("SELECT * FROM fct_quantity_by_customer").fetchdf()
actuals_df["month"] = pd.to_datetime(actuals_df["month"]).dt.to_period("M")
actuals_df["customer_id"] = actuals_df["customer_id"].astype(float).astype(int).astype(str)
actuals_df["country"] = actuals_df["country"].astype(str)

print(f"Forecast shape: {forecast_df.shape}")
print(f"Actuals shape: {actuals_df.shape}")

# === Merge on keys ===
merged_df = pd.merge(
    forecast_df,
    actuals_df,
    on=["month", "customer_id", "country"],
    how="inner",
    suffixes=("_forecast", "_actual")
)

print(f"Merged rows: {len(merged_df)}")

if merged_df.empty:
    print("\n❌ Merge resulted in 0 rows. Diagnosing keys...\n")
    print("Forecast months:", forecast_df["month"].unique())
    print("Actuals months:", actuals_df["month"].unique())

    print("\nForecast customer_ids:", forecast_df["customer_id"].unique())
    print("Actuals customer_ids:", actuals_df["customer_id"].unique())

    print("\nForecast countries:", forecast_df["country"].unique())
    print("Actuals countries:", actuals_df["country"].unique())
else:
    y_true = merged_df["total_quantity"]
    y_pred = merged_df["forecast_quantity"]

    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)

    print(f"\n✅ MAE:  {mae:.2f}")
    print(f"✅ RMSE: {rmse:.2f}")
