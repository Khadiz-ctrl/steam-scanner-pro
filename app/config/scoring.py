from app.config.loader import ConfigLoader

_settings = ConfigLoader.load()


class ScoringConfig:

    # --------------------------
    # Precio
    # --------------------------

    PRICE_VERY_CHEAP = _settings.scoring.price.very_cheap
    PRICE_CHEAP = _settings.scoring.price.cheap
    PRICE_SLIGHTLY_CHEAP = _settings.scoring.price.slightly_cheap

    # --------------------------
    # Volumen
    # --------------------------

    HIGH_VOLUME = _settings.scoring.volume.high
    MEDIUM_VOLUME = _settings.scoring.volume.medium
    LOW_VOLUME = _settings.scoring.volume.low

    # --------------------------
    # Historial
    # --------------------------

    LARGE_HISTORY = _settings.scoring.history.large
    MEDIUM_HISTORY = _settings.scoring.history.medium
    SMALL_HISTORY = _settings.scoring.history.small

    # --------------------------
    # Volatilidad
    # --------------------------

    LOW_VOLATILITY = _settings.scoring.volatility.low
    MEDIUM_VOLATILITY = _settings.scoring.volatility.medium
    HIGH_VOLATILITY = _settings.scoring.volatility.high