import sqlite3

conn = sqlite3.connect('temperaturas.db')
cursor = conn.cursor()

lista = [(23.50, '2018-08-27 15:10'),
    (21.90, '2018-08-27 10:58'),
    (18.20, '2018-08-27 19:23')]

cursor.executemany("""
INSERT INTO temperaturas (temp, data)
VALUES (?,?)
""", lista)

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
