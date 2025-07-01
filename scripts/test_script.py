import duckdb
import os

print("🧪 Testing DuckDB connection to a new file...")
TEST_DB = os.path.abspath("temp.duckdb")
try:
    con = duckdb.connect(TEST_DB)
    print("✅ Connection to new DB worked.")
    con.execute("CREATE TABLE test (id INTEGER)")
    con.execute("INSERT INTO test VALUES (1)")
    print(con.execute("SELECT * FROM test").fetchall())
except Exception as e:
    print("❌ Could not connect to new DB:")
    print(e)
