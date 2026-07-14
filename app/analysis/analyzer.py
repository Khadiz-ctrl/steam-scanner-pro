from app.analysis.moving_average import MovingAverage
from app.analysis.recommendation import Recommendation
from app.analysis.scorer import Scorer
from app.analysis.statistics import Statistics
from app.database.repository import PriceRepository


class Analyzer:

    def __init__(self):
        self.repository = PriceRepository()

    # ------------------------------------------------------------------
    # Repository
    # ------------------------------------------------------------------

    def get_last_price(self, skin):
        return self.repository.get_last_price(skin)

    def get_last_volume(self, skin):
        return self.repository.get_last_volume(skin)

    def get_price_history(self, skin):
        return self.repository.get_price_history(skin)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _get_prices(self, skin):

        history = self.get_price_history(skin)

        return [float(price) for _, price in history]

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def get_average_price(self, skin):
        return Statistics.average(
            self._get_prices(skin)
        )

    def get_moving_average(self, skin):
        return MovingAverage.calculate(
            self._get_prices(skin)
        )

    def get_price_difference_percent(self, skin):

        return Statistics.difference_percent(
            self.get_last_price(skin),
            self.get_moving_average(skin)
        )

    def get_trend(self, skin):
        return Statistics.trend(
            self._get_prices(skin)
        )

    def get_volatility(self, skin):
        return Statistics.volatility(
            self._get_prices(skin)
        )

    # ------------------------------------------------------------------
    # Analysis
    # ------------------------------------------------------------------

    def _build_analysis(self, skin):

        return {
            "skin": skin,
            "current_price": self.get_last_price(skin),
            "average_price": self.get_average_price(skin),
            "moving_average": self.get_moving_average(skin),
            "difference_percent": self.get_price_difference_percent(skin),
            "volume": self.get_last_volume(skin),
            "history": self.get_price_history(skin),
            "trend": self.get_trend(skin),
            "volatility": self.get_volatility(skin),
        }

    def _add_score(self, analysis):

        score_data = Scorer.calculate(analysis)

        analysis["score"] = score_data["score"]
        analysis["reasons"] = score_data["reasons"]
        analysis["debug"] = score_data["debug"]

    def _add_recommendation(self, analysis):

        analysis["recommendation"] = Recommendation.get(
            analysis["score"]
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def analyze_skin(self, skin):

        analysis = self._build_analysis(skin)

        self._add_score(analysis)

        self._add_recommendation(analysis)

        return analysis

    def analyze_watchlist(self, watchlist):

        analyses = []

        for item in watchlist:

            analysis = self.analyze_skin(item["skin"])

            analysis["target_price"] = item["target_price"]
            analysis["priority"] = item["priority"]

            analyses.append(analysis)

        return analyses