from app.analysis.scorer import Scorer
from app.domain.skin_analysis import SkinAnalysis


def make_analysis(
    difference=0,
    volume=50,
    history=30,
    volatility=2,
    trend="STABLE",
):

    analysis = SkinAnalysis(
        skin="Test Skin",
        current_price=100,
        average_price=100,
        moving_average=100,
        target_price=95,
        difference_percent=difference,
        volume=volume,
        trend=trend,
        volatility=volatility,
        history=[None] * history,
        priority=1,
    )

    return analysis


# -----------------------------
# Precio
# -----------------------------

def test_price_very_cheap():

    result = Scorer.calculate(
        make_analysis(difference=-6)
    )

    assert result["debug"]["Precio"] == 40


def test_price_cheap():

    result = Scorer.calculate(
        make_analysis(difference=-3)
    )

    assert result["debug"]["Precio"] == 25


def test_price_slightly_cheap():

    result = Scorer.calculate(
        make_analysis(difference=-0.5)
    )

    assert result["debug"]["Precio"] == 10


# -----------------------------
# Volumen
# -----------------------------

def test_high_volume():

    result = Scorer.calculate(
        make_analysis(volume=120)
    )

    assert result["debug"]["Volumen"] == 30


def test_medium_volume():

    result = Scorer.calculate(
        make_analysis(volume=70)
    )

    assert result["debug"]["Volumen"] == 20


def test_low_volume():

    result = Scorer.calculate(
        make_analysis(volume=10)
    )

    assert result["debug"]["Volumen"] == 10


# -----------------------------
# Historial
# -----------------------------

def test_large_history():

    result = Scorer.calculate(
        make_analysis(history=150)
    )

    assert result["debug"]["Historial"] == 30


# -----------------------------
# Volatilidad
# -----------------------------

def test_low_volatility():

    result = Scorer.calculate(
        make_analysis(volatility=0.5)
    )

    assert result["debug"]["Volatilidad"] == 20


# -----------------------------
# Score total
# -----------------------------

def test_total_score_exists():

    result = Scorer.calculate(
        make_analysis()
    )

    assert "TOTAL" in result["debug"]