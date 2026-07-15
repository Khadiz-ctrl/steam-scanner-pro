from dataclasses import dataclass, field

from app.domain.price_record import PriceRecord


@dataclass
class SkinAnalysis:
    """
    Representa el resultado completo del análisis
    de una skin.
    """

    # -------------------------
    # Identificación
    # -------------------------

    skin: str

    # -------------------------
    # Mercado
    # -------------------------

    current_price: float
    average_price: float
    moving_average: float
    difference_percent: float

    volume: int
    history: list[PriceRecord]

    trend: str
    volatility: float

    # -------------------------
    # Resultado del análisis
    # -------------------------

    score: int = 0

    recommendation: str = ""

    reasons: list[str] = field(default_factory=list)

    debug: dict[str, int] = field(default_factory=dict)

    # -------------------------
    # Watchlist
    # -------------------------

    target_price: float | None = None

    priority: int | None = None