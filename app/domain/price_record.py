from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class PriceRecord:
    """
    Representa una observación del mercado
    en un momento determinado.
    """

    created_at: datetime
    price: float
    volume: int