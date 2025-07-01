import duckdb
import pandas as pd
# import os

# File paths
csv_2010 = "data/csv/year_2009_2010.csv"
csv_2011 = "data/csv/year_2010_2011.csv"

# Read CSVs
df_2010 = pd.read_csv(csv_2010)
df_2011 = pd.read_csv(csv_2011)

# Combine them
df = pd.concat([df_2010, df_2011], ignore_index=True)
df.dropna(subset=["Customer ID"], inplace=True)

# Connect to the same DuckDB file dbt is using
con = duckdb.connect("dbt.duckdb")

# Write to DuckDB as a clean, raw table
con.execute("CREATE OR REPLACE TABLE raw_online_retail AS SELECT * FROM df")

print("✅ raw_online_retail table loaded into dbt.duckdb!")
