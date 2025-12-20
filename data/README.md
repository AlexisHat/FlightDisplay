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
## Notes

- Do **not** commit CSV or generated files.
- This directory is intentionally ignored by git, except for this README.

