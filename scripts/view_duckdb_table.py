import duckdb
import pandas as pd

# === CONFIGURATION ===
DUCKDB_PATH = "dbt.duckdb"        # Your database file
TABLE_NAME = "stg_online_retail"  # Change to any table you want
LIMIT_ROWS = 20                   # How many rows to preview
EXPORT_TO_CSV = False             # Change to True to save the result
CSV_OUTPUT_PATH = f"data/preview_{TABLE_NAME}.csv"

# === CONNECT TO DATABASE ===
try:
    con = duckdb.connect(DUCKDB_PATH)
    print(f"🔌 Connected to {DUCKDB_PATH}")
except Exception as e:
    print(f"❌ Failed to connect: {e}")
    exit()

# === QUERY THE TABLE ===
try:
    query = f"SELECT * FROM {TABLE_NAME} LIMIT {LIMIT_ROWS}"
    df = con.execute(query).fetchdf()
    print(f"\n📋 Preview of {TABLE_NAME} (first {LIMIT_ROWS} rows):\n")
    print(df)

    if EXPORT_TO_CSV:
        df.to_csv(CSV_OUTPUT_PATH, index=False)
        print(f"\n💾 Exported to {CSV_OUTPUT_PATH}")

except Exception as e:
    print(f"❌ Failed to query table '{TABLE_NAME}': {e}")
