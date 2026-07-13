class Recommendation:

    @staticmethod
    def get(score):

        if score >= 80:
            return "BUY"

        elif score >= 50:
            return "WATCH"

        return "SKIP"