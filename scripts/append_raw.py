import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")
RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")


def append_raw():
    print("\n🚀 Appending to raw_data.csv...")

    if not os.path.exists(STAGING_FILE):
        print("❌ staging_data.csv missing")
        return

    df_new = pd.read_csv(STAGING_FILE)
    print(f"📥 New rows: {len(df_new)}")

    if os.path.exists(RAW_FILE):
        try:
            df_existing = pd.read_csv(RAW_FILE)

            df_combined = pd.concat([df_existing, df_new], ignore_index=True)

            before = len(df_combined)

            df_combined.drop_duplicates(
                subset=["coin_id", "timestamp"],
                inplace=True
            )

            after = len(df_combined)
            print(f"🧹 Removed duplicates: {before - after}")

        except:
            print("⚠️ Corrupt raw file → recreating")
            df_combined = df_new
    else:
        print("🆕 Creating raw_data.csv")
        df_combined = df_new

    df_combined.to_csv(RAW_FILE, index=False)
    print(f"💾 Raw rows: {len(df_combined)}")


if __name__ == "__main__":
    append_raw()