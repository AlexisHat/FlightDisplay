from typing import List

from flightdisplay.domain.aircraft import Aircraft
from flightdisplay.domain.flight_state import FlightState
from flightdisplay.domain.position import Position
from flightdisplay.infrastructure.opensky_client import OpenSkyClient


class FlightService:
    def __init__(self, client: OpenSkyClient):
        self.client = client

    def get_flights_in_bbox(self, bbox) -> List[FlightState]:
        flights = []

        os = self.client.get_states_for_bbox(bbox)
        if os is None or os.states is None:
            return []

        for s in os.states:
            aircraft = Aircraft(icao24=s.icao24,
                                callsign=s.callsign.strip())
            posi = Position(
                lat=s.latitude,
                lon=s.longitude,
                altitude=s.geo_altitude
            )
            flights.append(
                FlightState(
                    aircraft=aircraft,
                    position=posi,
                    velocity=s.velocity,
                    heading=s.true_track
                )
            )
        return flights
