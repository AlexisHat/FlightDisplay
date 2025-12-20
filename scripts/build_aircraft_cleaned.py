from pathlib import Path
import pandas as pd
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent

DATA_DIR = SCRIPT_DIR.parent / "data"
INPUT_CSV  = DATA_DIR / "aircraft-database-complete-2025-08.csv"

df = pd.read_csv(INPUT_CSV,
                 on_bad_lines="skip",
                 low_memory=False)

#clean the colum names
df.columns = df.columns.str.strip("'")


#Just saving useful Columns
columns_keep = [
    "icao24", "country", "manufacturerName",
    "model", "operator", "operatorCallsign",
    "registration", "serialNumber", "typecode"
]

df = df[columns_keep]

df = df.replace({"": np.nan, " ": np.nan})

#making sure icao24 can function as a key for data
df = df.copy()

df["icao24"] = (
    df["icao24"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df = df[df["icao24"].notna() & (df["icao24"] != "")].copy()

df = df.drop_duplicates(subset=["icao24"], keep="first")

#saving as parquet
OUTPUT_PATH = DATA_DIR / "aircraft_cleaned.parquet"

df.to_parquet(OUTPUT_PATH, index=False)