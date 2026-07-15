from app.config import ScoringConfig
from app.messages import Messages


class Scorer:

    @staticmethod
    def calculate(analysis):

        score = 0
        reasons = []
        debug = {}

        # --------------------------
        # Precio
        # --------------------------

        points, reason = Scorer._score_price(
            analysis.difference_percent
        )

        score += points
        debug["Precio"] = points

        if reason:
            reasons.append(reason)

        # --------------------------
        # Volumen
        # --------------------------

        points, reason = Scorer._score_volume(
            analysis.volume
        )

        score += points
        debug["Volumen"] = points

        if reason:
            reasons.append(reason)

        # --------------------------
        # Historial
        # --------------------------

        points, reason = Scorer._score_history(
            len(analysis.history)
        )

        score += points
        debug["Historial"] = points

        if reason:
            reasons.append(reason)

        # --------------------------
        # Volatilidad
        # --------------------------

        points, reason = Scorer._score_volatility(
            analysis.volatility
        )

        score += points
        debug["Volatilidad"] = points

        if reason:
            reasons.append(reason)

        # --------------------------
        # Tendencia
        # --------------------------

        reasons.append(
            Scorer._trend_reason(
                analysis.trend
            )
        )

        debug["TOTAL"] = score

        return {
            "score": score,
            "reasons": reasons,
            "debug": debug,
        }

    # ----------------------------------------------------------
    # Price
    # ----------------------------------------------------------

    @staticmethod
    def _score_price(difference):

        if difference <= -5:
            return (
                ScoringConfig.PRICE_VERY_CHEAP,
                Messages.PRICE_VERY_CHEAP,
            )

        if difference <= -2:
            return (
                ScoringConfig.PRICE_CHEAP,
                Messages.PRICE_CHEAP,
            )

        if difference <= 0:
            return (
                ScoringConfig.PRICE_SLIGHTLY_CHEAP,
                Messages.PRICE_SLIGHTLY_CHEAP,
            )

        return 0, None

    # ----------------------------------------------------------
    # Volume
    # ----------------------------------------------------------

    @staticmethod
    def _score_volume(volume):

        if volume >= 100:
            return (
                ScoringConfig.HIGH_VOLUME,
                Messages.HIGH_VOLUME,
            )

        if volume >= 50:
            return (
                ScoringConfig.MEDIUM_VOLUME,
                Messages.MEDIUM_VOLUME,
            )

        return (
            ScoringConfig.LOW_VOLUME,
            Messages.LOW_VOLUME,
        )

    # ----------------------------------------------------------
    # History
    # ----------------------------------------------------------

    @staticmethod
    def _score_history(history_count):

        if history_count >= 100:
            return (
                ScoringConfig.LARGE_HISTORY,
                Messages.LARGE_HISTORY,
            )

        if history_count >= 30:
            return (
                ScoringConfig.MEDIUM_HISTORY,
                Messages.MEDIUM_HISTORY,
            )

        return (
            ScoringConfig.SMALL_HISTORY,
            Messages.SMALL_HISTORY,
        )

    # ----------------------------------------------------------
    # Volatility
    # ----------------------------------------------------------

    @staticmethod
    def _score_volatility(volatility):

        if volatility <= 1:
            return (
                ScoringConfig.LOW_VOLATILITY,
                Messages.LOW_VOLATILITY,
            )

        if volatility <= 3:
            return (
                ScoringConfig.MEDIUM_VOLATILITY,
                Messages.MEDIUM_VOLATILITY,
            )

        return 0, None

    # ----------------------------------------------------------
    # Trend
    # ----------------------------------------------------------

    @staticmethod
    def _trend_reason(trend):

        # Por ahora Statistics devuelve strings.
        # Cuando migremos a Enum, este método será el único que habrá que cambiar.

        if trend == "DOWN":
            return Messages.TREND_DOWN

        if trend == "UP":
            return Messages.TREND_UP

        return Messages.TREND_STABLE