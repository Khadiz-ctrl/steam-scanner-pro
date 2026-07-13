from app.database.database import Database
from app.analysis.scorer import Scorer


class Analyzer:

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

        resultado = self.db.cursor.fetchone()

        if resultado:
         return float(resultado[0])

        return None

    def get_price_history(self, skin):

        self.db.cursor.execute("""
            SELECT created_at, price
            FROM prices
            WHERE skin = ?
            ORDER BY created_at ASC
        """, (skin,))

        return self.db.cursor.fetchall()

    def get_average_price(self, skin):

        self.db.cursor.execute("""
            SELECT AVG(price)
            FROM prices
            WHERE skin = ?
        """, (skin,))

        resultado = self.db.cursor.fetchone()

        if resultado and resultado[0] is not None:
            return round(resultado[0], 2)

        return None
    

    def get_price_difference_percent(self, skin):

     current_price = self.get_last_price(skin)
     average_price = self.get_average_price(skin)
     if current_price is None or average_price is None:
        return None

     porcentaje = ((current_price - average_price) / average_price) * 100

     return round(porcentaje, 2)
    
    def analyze_skin(self, skin):

     analysis = {
        "skin": skin,
        "current_price": self.get_last_price(skin),
        "average_price": self.get_average_price(skin),
        "difference_percent": self.get_price_difference_percent(skin),
        "history": self.get_price_history(skin),
        "volume": self.get_last_volume(skin)
    }

     analysis["score"] = Scorer.calculate(analysis)

     return analysis
    
    def analyze_watchlist(self, skins):

     analyses = []

     for skin in skins:
        analysis = self.analyze_skin(skin)
        analyses.append(analysis)

     return analyses


    def get_last_volume(self, skin):
       self.db.cursor.execute("""
            SELECT volume
            FROM prices
            WHERE skin = ?
            ORDER BY created_at DESC
            LIMIT 1
        """, (skin,))
       
       resultado = self.db.cursor.fetchone()

       if resultado:
         return int(resultado[0])

         def get_last_volume(self, skin):
          self.db.cursor.execute("""
            SELECT volume
            FROM prices
            WHERE skin = ?
            ORDER BY created_at DESC
            LIMIT 1
        """, (skin,))
       
       resultado = self.db.cursor.fetchone()

       if resultado:
        return int(resultado[0])
