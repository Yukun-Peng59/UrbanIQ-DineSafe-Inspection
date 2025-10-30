import pandas as pd, os
from datetime import datetime

RAW_PATH = "data/raw/Dinesafe_raw_2025.csv"
OUT_PATH = f"data/raw/Dinesafe_snapshot_{datetime.now():%Y%m%d}.csv"

def load_data(path=RAW_PATH):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} records.")
    return df

def quick_validation(df):
    cols = ['EstablishmentID','InspectionDate','Status','Severity']
    missing = [c for c in cols if c not in df.columns]
    if missing:
        print('Missing columns:', missing)
    else:
        print('Schema validation passed.')

def save_snapshot(df):
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print('Snapshot saved:', OUT_PATH)

if __name__ == '__main__':
    df = load_data()
    quick_validation(df)
    save_snapshot(df)
