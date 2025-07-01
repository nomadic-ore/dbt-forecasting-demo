import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure output folder exists
os.makedirs("output/country_trends", exist_ok=True)

# Load data
df = pd.read_csv("data/fct_monthly_sales.csv")
df['month'] = pd.to_datetime(df['month'])

# Get list of unique countries
countries = df['country'].dropna().unique()

# Loop through each country
for country in countries:
    df_country = df[df["country"] == country].sort_values("month")

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(df_country["month"], df_country["total_units"], color='tab:blue', marker='o', label='Units')
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Total Units", color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.plot(df_country["month"], df_country["total_revenue"], color='tab:green', marker='s', label='Revenue')
    ax2.set_ylabel("Total Revenue", color='tab:green')
    ax2.tick_params(axis='y', labelcolor='tab:green')

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.title(f"Forecasted Sales Trend in {country}")
    plt.xticks(rotation=45)
    fig.tight_layout()

    # Clean filename
    safe_country = country.replace(" ", "_").replace("/", "_")
    plt.savefig(f"output/country_trends/{safe_country}_sales_trend.png")
    plt.close()

print("✅ Finished saving plots for all countries.")
