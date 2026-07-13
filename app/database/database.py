import sqlite3
from pathlib import Path


class Database:

    def __init__(self):
        Path("data").mkdir(exist_ok=True)
        self.conn = sqlite3.connect("data/steam_scanner.db")
        self.cursor = self.conn.cursor()

    def crear_tablas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                skin TEXT NOT NULL,
                price TEXT,
                volume TEXT,
                median_price TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def guardar_precio(self, skin, datos):
        self.cursor.execute("""
            INSERT INTO prices
            (skin, price, volume, median_price)
            VALUES (?, ?, ?, ?)
        """, (
            skin,
            datos.get("lowest_price"),
            datos.get("volume"),
            datos.get("median_price")
        ))

        self.conn.commit()

    def cerrar(self):
        self.conn.close()