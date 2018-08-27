

lista = [(23.50, '2018-08-27 15:10'),
    (21.90, '2018-08-27 10:58'),
    (18.20, '2018-08-27 19:23')]

cursor.executemany("""
    INSERT INTO temperaturas (temp, data)
    VALUES (?,?)
""", lista)

conn.commit()

cursor.execute("""
    SELECT * FROM temperaturas;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close();
