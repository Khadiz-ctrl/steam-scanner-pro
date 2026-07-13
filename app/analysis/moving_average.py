class MovingAverage:

    @staticmethod
    def calculate(prices, window=5):

        if not prices:
            return None

        recent_prices = prices[-window:]

        return round(sum(recent_prices) / len(recent_prices), 2)