from dataclasses import dataclass, field


@dataclass
class SkinAnalysis:

    skin: str

    current_price: float
    average_price: float
    moving_average: float

    difference_percent: float

    volume: int

    trend: str
    volatility: float

    history: list = field(default_factory=list)

    score: int = 0

    recommendation: str = ""

    reasons: list = field(default_factory=list)

    debug: dict = field(default_factory=dict)

    target_price: float | None = None

    priority: int = 0