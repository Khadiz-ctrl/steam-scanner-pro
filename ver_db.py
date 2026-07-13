import sqlite3

conexion = sqlite3.connect("data/steam_scanner.db")
cursor = conexion.cursor()

cursor.execute("""
SELECT price, typeof(price)
FROM prices
LIMIT 10
""")

for fila in cursor.fetchall():
    print(fila)

conexion.close()