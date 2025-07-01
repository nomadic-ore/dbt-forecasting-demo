import duckdb
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend (no GUI window)
import matplotlib.pyplot as plt

import os

# Try importing Plotly (optional)
try:
    import plotly.express as px
    has_plotly = True
except ImportError:
    has_plotly = False

# === Paths ===
DB_PATH = "dbt.duckdb"
CSV_EXPORT_PATH = "data/dropout_summary.csv"
PNG_EXPORT_PATH = "data/dropout_bar_chart.png"
HTML_EXPORT_PATH = "data/dropout_bar_chart.html"

# === Query audit_invalid_online_retail ===
print("📊 Connecting to DuckDB...")
con = duckdb.connect(DB_PATH)

query = """
    select issue_type, count(*) as num_rows
    from audit_invalid_online_retail
    group by issue_type
    order by num_rows desc
"""

print("📥 Querying dropout summary...")
df = con.execute(query).fetchdf()
print("\n📋 Dropout summary:\n")
print(df)

# === Export to CSV ===
df.to_csv(CSV_EXPORT_PATH, index=False)
print(f"\n✅ Saved summary to {CSV_EXPORT_PATH}")

# === Matplotlib Bar Chart ===
print("📈 Plotting with matplotlib...")
plt.figure(figsize=(8, 5))
plt.bar(df['issue_type'], df['num_rows'], color='skyblue')
plt.xlabel('Issue Type')
plt.ylabel('Number of Dropped Rows')
plt.title('Dropout Count by Issue Type')
plt.tight_layout()
plt.savefig(PNG_EXPORT_PATH)
plt.show()
print(f"✅ Saved static chart to {PNG_EXPORT_PATH}")

# === Plotly Interactive Chart (if available) ===
if has_plotly:
    print("🌀 Plotting with Plotly...")
    fig = px.bar(df, x='issue_type', y='num_rows',
                 title='Dropout Count by Issue Type (Interactive)',
                 labels={'issue_type': 'Reason for Dropout', 'num_rows': 'Count'},
                 color='issue_type')
    fig.write_html(HTML_EXPORT_PATH)
    print(f"✅ Saved interactive chart to {HTML_EXPORT_PATH}")
else:
    print("⚠️ Plotly not installed. Run 'pip install plotly' to enable interactive chart.")

