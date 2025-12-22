from typing import Optional

from flightdisplay.domain.aircraft import Aircraft


class AircraftRepository:
    def get_by_icao24(self, icao24: str) -> Optional[Aircraft]:
        raise NotImplementedError
