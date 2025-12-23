from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Aircraft:
    icao24: str
    country: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    operator: Optional[str] = None
    registration: Optional[str] = None
    typecode: Optional[str] = None
