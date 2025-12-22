from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Position:
    lat: float
    lon: float
    altitude: Optional[float] = None
