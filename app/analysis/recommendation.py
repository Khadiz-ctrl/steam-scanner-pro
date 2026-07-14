from app.config import ScoringConfig


class Recommendation:

    @staticmethod
    def get(score):

        if score >= ScoringConfig.BUY_THRESHOLD:
            return "BUY"

        if score >= ScoringConfig.WATCH_THRESHOLD:
            return "WATCH"

        return "SKIP"