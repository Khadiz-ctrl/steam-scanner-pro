from app.config import Config


class Scorer:

    @staticmethod
    def calculate(analysis):

        score = 0
        reasons = []

        difference = analysis["difference_percent"]
        volume = analysis["volume"]
        history_count = len(analysis["history"])
        volatility = analysis["volatility"]
        trend = analysis["trend"]

        # Precio
        if difference <= -5:
            score += Config.PRICE_VERY_CHEAP
            reasons.append("Precio muy por debajo del promedio")

        elif difference <= -2:
            score += Config.PRICE_CHEAP
            reasons.append("Precio por debajo del promedio")

        elif difference <= 0:
            score += Config.PRICE_SLIGHTLY_CHEAP
            reasons.append("Precio ligeramente por debajo del promedio")

        # Volumen
        if volume >= 100:
            score += Config.HIGH_VOLUME
            reasons.append("Volumen alto")

        elif volume >= 50:
            score += Config.MEDIUM_VOLUME
            reasons.append("Buen volumen")

        else:
            score += Config.LOW_VOLUME
            reasons.append("Volumen bajo")

        # Historial
        if history_count >= 100:
            score += Config.LARGE_HISTORY
            reasons.append("Historial amplio")

        elif history_count >= 30:
            score += Config.MEDIUM_HISTORY
            reasons.append("Historial suficiente")

        else:
            score += Config.SMALL_HISTORY
            reasons.append("Historial corto")

        # Volatilidad
        if volatility <= 1:
            score += Config.LOW_VOLATILITY
            reasons.append("Baja volatilidad")

        elif volatility <= 3:
            score += Config.MEDIUM_VOLATILITY
            reasons.append("Volatilidad moderada")

        # Tendencia
        if trend == "DOWN":
            reasons.append("Tendencia bajista")
        elif trend == "UP":
            reasons.append("Tendencia alcista")
        else:
            reasons.append("Tendencia estable")

        return {
            "score": score,
            "reasons": reasons
        }