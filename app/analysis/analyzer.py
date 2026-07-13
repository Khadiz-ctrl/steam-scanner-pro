from app.analysis.scorer import Scorer
from app.analysis.statistics import Statistics
from app.database.repository import PriceRepository


class Analyzer:

    def __init__(self):
        self.repository = PriceRepository()

    def get_last_price(self, skin):
        return self.repository.get_last_price(skin)

    def get_last_volume(self, skin):
        return self.repository.get_last_volume(skin)

    def get_price_history(self, skin):
        return self.repository.get_price_history(skin)

    def get_average_price(self, skin):

        history = self.get_price_history(skin)

        prices = [float(price) for _, price in history]

        return Statistics.average(prices)

    def get_price_difference_percent(self, skin):

        current_price = self.get_last_price(skin)
        average_price = self.get_average_price(skin)

        return Statistics.difference_percent(
            current_price,
            average_price
        )

    def get_trend(self, skin):

        history = self.get_price_history(skin)

        prices = [float(price) for _, price in history]

        return Statistics.trend(prices)

    def get_volatility(self, skin):

        history = self.get_price_history(skin)

        prices = [float(price) for _, price in history]

        return Statistics.volatility(prices)

    def analyze_skin(self, skin):

        analysis = {
            "skin": skin,
            "current_price": self.get_last_price(skin),
            "average_price": self.get_average_price(skin),
            "difference_percent": self.get_price_difference_percent(skin),
            "volume": self.get_last_volume(skin),
            "history": self.get_price_history(skin),
            "trend": self.get_trend(skin),
            "volatility": self.get_volatility(skin),
        }

        score_data = Scorer.calculate(analysis)

        analysis["score"] = score_data["score"]
        analysis["reasons"] = score_data["reasons"]

        return analysis

    def analyze_watchlist(self, watchlist):

        analyses = []

        for item in watchlist:

            analysis = self.analyze_skin(item["skin"])

            analysis["target_price"] = item["target_price"]
            analysis["priority"] = item["priority"]

            analyses.append(analysis)

        return analyses