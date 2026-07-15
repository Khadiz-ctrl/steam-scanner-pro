from app.analysis.statistics import Statistics


def test_average():

    prices = [10, 20, 30]

    result = Statistics.average(prices)

    assert result == 20


def test_difference_percent():

    current = 90
    average = 100

    result = Statistics.difference_percent(current, average)

    assert result == -10


def test_trend_up():

    prices = [10, 11, 12, 13]

    result = Statistics.trend(prices)

    assert result == "UP"


def test_trend_down():

    prices = [13, 12, 11, 10]

    result = Statistics.trend(prices)

    assert result == "DOWN"


def test_volatility():

    prices = [10, 12, 15, 11]

    result = Statistics.volatility(prices)

    assert result == 5