from pathlib import Path
from typing import List

from flightdisplay.domain.aircraft import Aircraft
from flightdisplay.domain.flight_state import FlightState
from flightdisplay.domain.position import Position
from flightdisplay.infrastructure.db import connect
from flightdisplay.infrastructure.aircraft_repository_sqlite import AircraftRepositorySQLite
from flightdisplay.infrastructure.opensky_client import OpenSkyClient


class FlightService:
    def __init__(self, client: OpenSkyClient, db_path: Path):
        self.client = client
        print(db_path)
        self.conn = connect(db_path)
        self.repo = AircraftRepositorySQLite(self.conn)

    def close(self) -> None:
        self.conn.close()

    def get_flights_in_bbox(self, bbox) -> List[FlightState]:
        flights = []

        os = self.client.get_states_for_bbox(bbox)
        if os is None or os.states is None:
            return []

        for s in os.states:
            aircraft = self.repo.get_by_icao24(s.icao24)

            if aircraft is None:
                aircraft = Aircraft(icao24=s.icao24)

            posi = Position(
                lat=s.latitude,
                lon=s.longitude,
                altitude=s.geo_altitude
            )
            flights.append(
                FlightState(
                    aircraft=aircraft,
                    position=posi,
                    callsign=s.callsign.strip(),
                    velocity=s.velocity,
                    heading=s.true_track
                )
            )
        return flights
