from typing import Optional
import sqlite3

from flightdisplay.domain.aircraft import Aircraft
from flightdisplay.domain.repos.aircraft_repository import AircraftRepository

class AircraftRepositorySQLite(AircraftRepository):
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def get_by_icao24(self, icao24: str) -> Optional[Aircraft]:
        cur = self._conn.execute(
            """
            SELECT country, manufacturer, model, operator, registration, typecode
            FROM aircraft
            WHERE icao24 = ?
            """,
            (icao24.lower().strip(),),
        )
        row = cur.fetchone()
        if row is None:
            return None

        return Aircraft(
            icao24=icao24,
            country=row[0],
            manufacturer=row[1],
            model=row[2],
            operator=row[3],
            registration=row[4],
            typecode=row[5]
        )
