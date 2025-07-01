import duckdb

con = duckdb.connect("dbt.duckdb")

df = con.execute("SELECT * FROM fct_quantity_by_customer LIMIT 10").fetchdf()
print(df)
