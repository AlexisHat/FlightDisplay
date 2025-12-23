import sqlite3
from pathlib import Path
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"

PARQUET_PATH = DATA_DIR / "aircraft_cleaned.parquet"
DB_PATH = DATA_DIR / "aircraft.sqlite3"


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS aircraft (
      icao24 TEXT PRIMARY KEY,
      country TEXT,
      manufacturer TEXT,
      model TEXT,
      operator TEXT,
      registration TEXT,
      typecode TEXT
    );
    """)
    conn.commit()


def load_parquet_into_db():
    # Parquet laden
    df = pd.read_parquet(PARQUET_PATH)

    # Spalten auf DB-Schema anpassen
    df = df[[
        "icao24",
        "country",
        "manufacturerName",
        "model",
        "operator",
        "registration",
        "typecode",
    ]]

    df = df.rename(columns={
        "manufacturerName": "manufacturer"
    })

    conn = connect(DB_PATH)
    init_schema(conn)

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT OR REPLACE INTO aircraft (
                icao24,
                country,
                manufacturer,
                model,
                operator,
                registration,
                typecode
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(row["icao24"])
                .strip()
                .strip("'")
                .strip('"')
                .lower(),
                row["country"],
                row["manufacturer"],
                row["model"],
                row["operator"],
                row["registration"],
                row["typecode"],
            )
        )

    conn.commit()
    conn.close()

    print(f" {len(df)} Flugzeuge in die Datenbank geschrieben.")


if __name__ == "__main__":
    load_parquet_into_db()
