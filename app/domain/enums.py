from enum import Enum


class Recommendation(Enum):
    BUY = "BUY"
    WATCH = "WATCH"
    SKIP = "SKIP"


class Trend(Enum):
    UP = "UP"
    DOWN = "DOWN"
    STABLE = "STABLE"