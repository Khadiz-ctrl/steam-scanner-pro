from app.config.scoring import ScoringConfig


class Scorer:

    @staticmethod
    def calculate(analysis):

        score = 0
        reasons = []
        debug = {}

        difference = analysis["difference_percent"]
        volume = analysis["volume"]
        history_count = len(analysis["history"])
        volatility = analysis["volatility"]
        trend = analysis["trend"]

        # -----------------------
        # Precio
        # -----------------------

        points = 0

        if difference <= -5:
            points = ScoringConfig.PRICE_VERY_CHEAP
            reasons.append("Precio muy por debajo del promedio")

        elif difference <= -2:
            points = ScoringConfig.PRICE_CHEAP
            reasons.append("Precio por debajo del promedio")

        elif difference <= 0:
            points = ScoringConfig.PRICE_SLIGHTLY_CHEAP
            reasons.append("Precio ligeramente por debajo del promedio")

        score += points
        debug["Precio"] = points

        # -----------------------
        # Volumen
        # -----------------------

        points = 0

        if volume >= 100:
            points = ScoringConfig.HIGH_VOLUME
            reasons.append("Volumen alto")

        elif volume >= 50:
            points = ScoringConfig.MEDIUM_VOLUME
            reasons.append("Buen volumen")

        else:
            points = ScoringConfig.LOW_VOLUME
            reasons.append("Volumen bajo")

        score += points
        debug["Volumen"] = points

        # -----------------------
        # Historial
        # -----------------------

        points = 0

        if history_count >= 100:
            points = ScoringConfig.LARGE_HISTORY
            reasons.append("Historial amplio")

        elif history_count >= 30:
            points = ScoringConfig.MEDIUM_HISTORY
            reasons.append("Historial suficiente")

        else:
            points = ScoringConfig.SMALL_HISTORY
            reasons.append("Historial corto")

        score += points
        debug["Historial"] = points

        # -----------------------
        # Volatilidad
        # -----------------------

        points = 0

        if volatility <= 1:
            points = ScoringConfig.LOW_VOLATILITY
            reasons.append("Baja volatilidad")

        elif volatility <= 3:
            points = ScoringConfig.MEDIUM_VOLATILITY
            reasons.append("Volatilidad moderada")

        score += points
        debug["Volatilidad"] = points

        if trend == "DOWN":
            reasons.append("Tendencia bajista")

        elif trend == "UP":
            reasons.append("Tendencia alcista")

        else:
            reasons.append("Tendencia estable")

        debug["TOTAL"] = score

        return {
            "score": score,
            "reasons": reasons,
            "debug": debug
        }