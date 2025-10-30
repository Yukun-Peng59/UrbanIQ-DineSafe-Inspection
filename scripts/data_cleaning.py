import pandas as pd

RAW_FILE = "data/raw/Dinesafe_raw_2025.csv"
OUTPUT_FILE = "data/cleaned/dinesafe_cleaned.csv"

def clean_dinesafe():
    df = pd.read_csv(RAW_FILE)
    df.drop_duplicates(subset=['EstablishmentID','InspectionDate','InfractionDetails'], inplace=True)
    df['InspectionDate'] = pd.to_datetime(df['InspectionDate'], errors='coerce')
    df['Status'] = df['Status'].str.strip().str.title()
    df['Severity'] = df['Severity'].str.upper().fillna('NA')
    df['InfractionDetails'] = df['InfractionDetails'].fillna('No violation recorded')
    df = df[(df['Latitude'].between(43,44)) & (df['Longitude'].between(-79.7,-79.1))]
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data saved to {OUTPUT_FILE} with {len(df)} rows")

if __name__ == '__main__':
    clean_dinesafe()
