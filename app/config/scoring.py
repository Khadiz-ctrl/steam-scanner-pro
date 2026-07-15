from app.config.loader import ConfigLoader

_settings = ConfigLoader.load()


class ScoringConfig:

    # --------------------------------------------------
    # Recommendation thresholds
    # --------------------------------------------------

    BUY_THRESHOLD = 80
    WATCH_THRESHOLD = 50

    # --------------------------------------------------
    # Price
    # --------------------------------------------------

    PRICE_VERY_CHEAP = _settings.scoring.price.very_cheap
    PRICE_CHEAP = _settings.scoring.price.cheap
    PRICE_SLIGHTLY_CHEAP = _settings.scoring.price.slightly_cheap

    # --------------------------------------------------
    # Volume
    # --------------------------------------------------

    HIGH_VOLUME = _settings.scoring.volume.high
    MEDIUM_VOLUME = _settings.scoring.volume.medium
    LOW_VOLUME = _settings.scoring.volume.low

    # --------------------------------------------------
    # History
    # --------------------------------------------------

    LARGE_HISTORY = _settings.scoring.history.large
    MEDIUM_HISTORY = _settings.scoring.history.medium
    SMALL_HISTORY = _settings.scoring.history.small

    # --------------------------------------------------
    # Volatility
    # --------------------------------------------------

    LOW_VOLATILITY = _settings.scoring.volatility.low
    MEDIUM_VOLATILITY = _settings.scoring.volatility.medium
    HIGH_VOLATILITY = _settings.scoring.volatility.high