class Statistics:

    @staticmethod
    def average(prices):

        if not prices:
            return None

        return round(sum(prices) / len(prices), 2)

    @staticmethod
    def difference_percent(current_price, average_price):

        if current_price is None or average_price is None:
            return None

        percentage = ((current_price - average_price) / average_price) * 100

        return round(percentage, 2)

    @staticmethod
    def trend(prices):

        if len(prices) < 2:
            return "UNKNOWN"

        difference = prices[-1] - prices[0]

        if difference > 0.5:
            return "UP"

        elif difference < -0.5:
            return "DOWN"

        return "STABLE"

    @staticmethod
    def volatility(prices):

        if len(prices) < 2:
            return 0

        return round(max(prices) - min(prices), 2)