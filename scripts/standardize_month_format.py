import pandas as pd
from pathlib import Path

# Define paths
DATA_DIR = Path("data")
FILES = [
    ("fct_monthly_sales.csv", ["month"]),
    ("forecast_quantity_ensemble.csv", ["month"])
]

def standardize_month_format(file_path, date_cols):
    full_path = DATA_DIR / file_path
    if not full_path.exists():
        print(f"❌ File not found: {full_path}")
        return

    print(f"📄 Processing: {file_path}")
    df = pd.read_csv(full_path)

    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col]).dt.strftime("%Y-%m-%d")
            print(f"✅ Converted '{col}' to YYYY-MM-DD format.")
        except Exception as e:
            print(f"❌ Failed to convert '{col}' in {file_path}: {e}")

    # Overwrite original file
    df.to_csv(full_path, index=False)
    print(f"💾 Saved updated file to: {full_path}\n")

# Run standardization for each file
for filename, date_cols in FILES:
    standardize_month_format(filename, date_cols)

print("🏁 All done!")
