import sqlite3

conn = sqlite3.connect('temperaturas.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE temperaturas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    temp DECIMAL(5,2) NOT NULL,
    data DATE NOT NULL
);
""")

conn.close();
