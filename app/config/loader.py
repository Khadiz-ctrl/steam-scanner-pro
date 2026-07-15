from pathlib import Path

import yaml

from app.config.settings import (
    HistoryConfig,
    PriceConfig,
    RecommendationConfig,
    ReportsSettings,
    ScannerSettings,
    ScoringSettings,
    Settings,
    VolumeConfig,
    VolatilityConfig,
)


class ConfigLoader:

    @staticmethod
    def load(path: str | Path = "config/default.yaml") -> Settings:

        path = Path(path)

        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        scoring = data["scoring"]

        return Settings(
            scoring=ScoringSettings(
                price=PriceConfig(**scoring["price"]),
                volume=VolumeConfig(**scoring["volume"]),
                history=HistoryConfig(**scoring["history"]),
                volatility=VolatilityConfig(**scoring["volatility"]),
                recommendation=RecommendationConfig(
                    **data["recommendation"]
                ),
            ),
            scanner=ScannerSettings(**data["scanner"]),
            reports=ReportsSettings(**data["reports"]),
        )