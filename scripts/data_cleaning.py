pip install gdown

# ---------- Step 1: Import Libraries ----------
import pandas as pd
import numpy as np
import gdown
import os

# ---------- Step 2: Download Raw Dataset from Google Drive ----------
# File is stored in Google Drive (public share link)
file_id = "1RXZzlH4e3TKkssKzIfO6slSq_Mg3gm9x"
raw_path = "DineSafe.csv"

# Download the dataset if not already present
if not os.path.exists(raw_path):
    print("⬇️ Downloading DineSafe dataset from Google Drive...")
    gdown.download(id=file_id, output=raw_path, quiet=False)
else:
    print("✅ Found existing local file. Skipping download.")

# ---------- Step 3: Load Dataset ----------
print("\n📂 Loading dataset...")
df = pd.read_csv(raw_path)
print(f"✅ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

# ---------- Step 4: Initial Overview ----------
print("🔍 Preview of raw data:")
print(df.head(), "\n")
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# ---------- Step 5: Handle Missing Values ----------
print("🔧 Handling missing values...")

# Delete records with missing key fields
df = df.dropna(subset=["Inspection ID", "Inspection Date", "Establishment Name"])

#  Fill in the missing logically
df["Infraction Details"] = df["Infraction Details"].fillna("No Infraction")
df["Severity"] = df["Severity"].fillna("No Infraction")
df["Action"] = df["Action"].fillna("None")
df["Outcome"] = df["Outcome"].fillna("Pending/No Action")
df["Amount Fined"] = df["Amount Fined"].fillna(0)

print("✅ Missing values handled.\n")
print(df.isnull().sum())


# ---------- Step 6: Remove Duplicates ----------

dup_count = df.duplicated().sum()
print(f"🔍 Found {dup_count} duplicate rows before removal.")

before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"✅ Removed {before - after} duplicate rows.\n")


# ---------- Step 7: Correct Data Types ----------
# Convert date columns
for col in df.columns:
    if 'Date' in col:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        except Exception:
            pass

print("✅ Data types standardized.\n")

# ---------- Step 8: Clean Text Fields ----------
text_cols = ['Establishment Name', 'Address', 'City', 'Infraction Details']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.title()

print("✅ Text fields cleaned.\n")

# ---------- Step 9: Export Cleaned Dataset ----------
clean_dir = "data_cleaned"
os.makedirs(clean_dir, exist_ok=True)
clean_path = os.path.join(clean_dir, "DineSafe_Cleaned.csv")
df.to_csv(clean_path, index=False)

print(f"💾 Cleaned dataset saved to: {clean_path}")
print(f"✅ Final shape: {df.shape[0]} rows, {df.shape[1]} columns")
