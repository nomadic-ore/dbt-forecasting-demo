import duckdb

print("🧪 Testing SELECT on fct_quantity_by_customer")

try:
    con = duckdb.connect("dbt.duckdb")
    df = con.execute("SELECT * FROM fct_quantity_by_customer LIMIT 5").fetchdf()
    print(df)
    print("✅ Query succeeded with", len(df), "rows")
except Exception as e:
    print("❌ Query failed:")
    print(e)
