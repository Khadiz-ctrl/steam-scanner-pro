from app.database.database import Database


class PriceRepository:

    def __init__(self):
        self.db = Database()

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

    def get_price_history(self, skin):

        self.db.cursor.execute("""
            SELECT created_at, price
            FROM prices
            WHERE skin = ?
            ORDER BY created_at ASC
        """, (skin,))

        return self.db.cursor.fetchall()