from dataclasses import dataclass


@dataclass(slots=True)
class PriceConfig:
    very_cheap: int
    cheap: int
    slightly_cheap: int


@dataclass(slots=True)
class VolumeConfig:
    high: int
    medium: int
    low: int


@dataclass(slots=True)
class HistoryConfig:
    large: int
    medium: int
    small: int


@dataclass(slots=True)
class VolatilityConfig:
    low: int
    medium: int
    high: int


@dataclass(slots=True)
class ScoringSettings:
    price: PriceConfig
    volume: VolumeConfig
    history: HistoryConfig
    volatility: VolatilityConfig


@dataclass(slots=True)
class ScannerSettings:
    refresh_seconds: int


@dataclass(slots=True)
class ReportsSettings:
    output_folder: str


@dataclass(slots=True)
class Settings:
    scoring: ScoringSettings
    scanner: ScannerSettings
    reports: ReportsSettings