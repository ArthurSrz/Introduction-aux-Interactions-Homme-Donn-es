import duckdb
cursor = duckdb.connect()
print(cursor.execute('SELECT 42').fetchall())
SELECT * FROM read_json_auto('http://api.worldbank.org/v2/indicators/NY.GDP.MKTP.CD?format=json');