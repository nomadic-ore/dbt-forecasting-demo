import pandas as pd
from pathlib import Path

# Base directory
base_dir = Path(__file__).resolve().parent.parent  # Moves up from /scripts/ to project root
data_dir = base_dir / "data"
output_dir = data_dir / "csv"
output_dir.mkdir(parents=True, exist_ok=True)

# Excel file path
excel_path = data_dir / "online_retail_II.xlsx"

# Sheet names
sheet_names = ["Year 2009-2010", "Year 2010-2011"]

# Convert each sheet to a CSV file
for sheet in sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet)
    clean_name = sheet.lower().replace(" ", "_").replace("-", "_")
    csv_path = output_dir / f"{clean_name}.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Saved {sheet} → {csv_path}")
