import sqlite3
from pathlib import Path

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS aircraft (
  icao24 TEXT PRIMARY KEY,
  country TEXT,
  manufacturer TEXT,
  model TEXT,
  operator TEXT,
  registration TEXT,
  typecode TEXT
);

CREATE INDEX IF NOT EXISTS idx_aircraft_icao24 ON aircraft(icao24);
"""

def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)
    conn.commit()
