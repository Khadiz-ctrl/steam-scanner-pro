import sqlite3

conexion = sqlite3.connect("data/steam_scanner.db")

cursor = conexion.cursor()

cursor.execute("""
SELECT skin, price, volume, created_at
FROM prices
ORDER BY id DESC
""")

for fila in cursor.fetchall():
    print(fila)

conexion.close()