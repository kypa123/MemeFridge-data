import psycopg2
import os

conn = psycopg2.connect(os.getenv('POSTGRES_CONNECTION'))

cur = conn.cursor()

cur.execute("select * from test")

result = cur.fetchone();
print(result);