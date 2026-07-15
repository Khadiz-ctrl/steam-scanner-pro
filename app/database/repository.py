from datetime import datetime

from app.database.database import Database
from app.domain.price_record import PriceRecord


class PriceRepository:

    def __init__(self):
        self.db = Database()

    # ---------------------------------------------------------
    # Last Price
    # ---------------------------------------------------------

    def get_last_price(self, skin):

        self.db.cursor.execute("""
            SELECT price
            FROM prices
            WHERE skin = ?
            ORDER BY created_at DESC
            LIMIT 1
        """, (skin,))

        result = self.db.cursor.fetchone()

        if result:
            return float(result[0])

        return None

    # ---------------------------------------------------------
    # Last Volume
    # ---------------------------------------------------------

    def get_last_volume(self, skin):

        self.db.cursor.execute("""
            SELECT volume
            FROM prices
            WHERE skin = ?
            ORDER BY created_at DESC
            LIMIT 1
        """, (skin,))

        result = self.db.cursor.fetchone()

        if result:
            return int(result[0])

        return None

    # ---------------------------------------------------------
    # Price History
    # ---------------------------------------------------------

    def get_price_history(self, skin):

        self.db.cursor.execute("""
            SELECT created_at, price, volume
            FROM prices
            WHERE skin = ?
            ORDER BY created_at ASC
        """, (skin,))

        rows = self.db.cursor.fetchall()

        history = []

        for created_at, price, volume in rows:

            try:
                created_at = datetime.fromisoformat(created_at)
            except Exception:
                # Si SQLite devuelve un formato distinto,
                # conservamos el valor original.
                pass

            history.append(
                PriceRecord(
                    created_at=created_at,
                    price=float(price),
                    volume=int(volume),
                )
            )

        return history