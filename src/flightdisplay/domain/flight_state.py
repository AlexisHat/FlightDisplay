from dataclasses import dataclass
from .position import Position
from .aircraft import Aircraft
from typing import Optional

@dataclass(frozen=True)
class FlightState:
    aircraft: Aircraft
    position: Position
    callsign: Optional[str] = None
    velocity: Optional[float] = None
    heading: Optional[float] = None
