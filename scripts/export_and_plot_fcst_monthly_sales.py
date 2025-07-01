import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import os

# Try importing Plotly (optional)
try:
    import plotly.express as px
    has_plotly = True
except ImportError:
    has_plotly = False

# === File Paths ===
DB_PATH = "dbt.duckdb"
CSV_PATH = "data/fct_monthly_sales.csv"
PLOT_PNG_PATH = "data/fct_monthly_sales_plot.png"
PLOT_HTML_PATH = "data/fct_monthly_sales_plot.html"

# === Query the Forecasting Model ===
print("📊 Connecting to DuckDB...")
con = duckdb.connect(DB_PATH)

query = """
    SELECT *
    FROM fcst_monthly_sales
    ORDER BY month, country
"""

print("📥 Querying fct_monthly_sales...")
df = con.execute(query).fetchdf()

# === Export to CSV ===
df.to_csv(CSV_PATH, index=False)
print(f"✅ Saved to {CSV_PATH}")

# === Matplotlib Static Plot ===
print("📈 Generating static plot...")
plt.figure(figsize=(10, 5))

# Optional: plot just top 1 country
top_country = df['country'].value_counts().idxmax()
df_top = df[df['country'] == top_country]

plt.plot(df_top['month'], df_top['total_revenue'], marker='o')
plt.title(f"Monthly Revenue - {top_country}")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(PLOT_PNG_PATH)
plt.show()
print(f"✅ Static chart saved to {PLOT_PNG_PATH}")

# === Plotly Interactive Chart ===
if has_plotly:
    print("🌀 Generating interactive plot...")
    fig = px.line(
        df_top,
        x='month',
        y='total_revenue',
        color='country',
        title=f"Interactive Monthly Revenue - {top_country}",
        labels={'month': 'Month', 'total_revenue': 'Revenue'}
    )
    fig.write_html(PLOT_HTML_PATH)
    print(f"✅ Interactive chart saved to {PLOT_HTML_PATH}")
else:
    print("⚠️ Plotly not installed. Run 'pip install plotly' to enable interactive chart.")
