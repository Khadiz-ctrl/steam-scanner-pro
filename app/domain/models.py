from dataclasses import dataclass, field

from app.domain.enums import Recommendation, Trend
from app.domain.price_record import PriceRecord


@dataclass(slots=True)
class SkinAnalysis:

    skin: str

    current_price: float
    average_price: float
    moving_average: float
    difference_percent: float

    volume: int
    history: list[PriceRecord]

    trend: Trend
    volatility: float

    score: int = 0

    recommendation: Recommendation = Recommendation.SKIP

    reasons: list[str] = field(default_factory=list)

    debug: dict[str, int] = field(default_factory=dict)

    target_price: float | None = None

    priority: int | None = None