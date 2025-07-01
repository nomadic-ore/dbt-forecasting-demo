import duckdb

con = duckdb.connect("dbt.duckdb")
df = con.execute("SELECT * FROM audit_invalid_online_retail LIMIT 100").fetchdf()
print(df)