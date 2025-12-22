from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Aircraft:
    icao24: str
    callsign: Optional[str] = None
