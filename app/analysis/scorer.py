class Scorer:

    @staticmethod
    def calculate(analysis):

        score = 0

        difference = analysis["difference_percent"]
        volume = analysis["volume"]
        history_count = len(analysis["history"])

        # Precio
        if difference <= -5:
            score += 40
        elif difference <= -2:
            score += 25
        elif difference <= 0:
            score += 10

        # Volumen
        if volume >= 100:
            score += 30
        elif volume >= 50:
            score += 20
        else:
            score += 10

        # Historial
        if history_count >= 100:
            score += 30
        elif history_count >= 30:
            score += 20
        else:
            score += 10

        return score