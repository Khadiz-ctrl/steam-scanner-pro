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
            score += 40
            reasons.append("Precio muy por debajo del promedio")

        elif difference <= -2:
            score += 25
            reasons.append("Precio por debajo del promedio")

        elif difference <= 0:
            score += 10
            reasons.append("Precio ligeramente por debajo del promedio")

        # Volumen
        if volume >= 100:
            score += 30
            reasons.append("Volumen alto")

        elif volume >= 50:
            score += 20
            reasons.append("Buen volumen")

        else:
            score += 10
            reasons.append("Volumen bajo")

        # Historial
        if history_count >= 100:
            score += 30
            reasons.append("Historial amplio")

        elif history_count >= 30:
            score += 20
            reasons.append("Historial suficiente")

        else:
            score += 10
            reasons.append("Historial corto")

        # Volatilidad
        if volatility <= 1:
            score += 20
            reasons.append("Baja volatilidad")

        elif volatility <= 3:
            score += 10
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
    

