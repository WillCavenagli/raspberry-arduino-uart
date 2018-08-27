import sqlite3

conn = sqlite3.connect('temperaturas.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT * FROM temperaturas;
    """)

for linha in cursor.fetchall():
    print(linha)

conn.close()
