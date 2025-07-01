import pandas as pd
import matplotlib.pyplot as plt
import os

# ✅ Load forecast data
df = pd.read_csv("data/forecast_quantity_ensemble.csv")
df['month'] = pd.to_datetime(df['month'])

# 🧼 Ensure customer_id is a string for labeling
df['customer_id'] = df['customer_id'].astype(str)

# 📁 Create output folder if it doesn't exist
output_dir = "output/forecast_charts"
os.makedirs(output_dir, exist_ok=True)

# 🔁 Loop over each customer
for (customer_id, country), group in df.groupby(['customer_id', 'country']):
    group_sorted = group.sort_values('month')

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(group_sorted['month'], group_sorted['forecast_quantity'], marker='o', label='Forecast Quantity', color='tab:blue')
    plt.title(f"Forecasted Quantity for Customer {customer_id} ({country})")
    plt.xlabel("Month")
    plt.ylabel("Forecast Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save chart
    filename = f"{output_dir}/customer_{customer_id}_{country.replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()

print(f"✅ Charts saved to: {output_dir}")
