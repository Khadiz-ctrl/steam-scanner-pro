from app.analysis.recommendation import Recommendation


def test_buy():

    assert Recommendation.get(80) == "BUY"
    assert Recommendation.get(100) == "BUY"


def test_watch():

    assert Recommendation.get(50) == "WATCH"
    assert Recommendation.get(79) == "WATCH"


def test_skip():

    assert Recommendation.get(49) == "SKIP"
    assert Recommendation.get(0) == "SKIP"