# Data Directory

This directory contains **local data files** required to run *flight-display*.
The files in this folder are **not tracked by git**.

## Required data

### OpenSky Aircraft Database

1. Download the latest **monthly complete snapshot**  
   `aircraft-Database-complete-2025-08.csv` from:
   https://opensky-network.org/datasets/#metadata/

2. Place the CSV file in this directory:
    data/...
 

## Data processing

After downloading the CSV, generate the cleaned dataset using the provided script:

```bash
python scripts/build_aircraft_cleaned.py
```

2. Load the cleaned data into SQLite
Next, load the cleaned Parquet file into a local SQLite database:

python scripts/load_aircraft_into_sqlite.py
```bash
python scripts/load_aircraft_into_sqlite.py
```
This will create: data/aircraft.sqlite3
and populate the aircraft table.
## Notes

- Do **not** commit CSV or generated files.
- This directory is intentionally ignored by git, except for this README.

