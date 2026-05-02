# import os
# import pandas as pd

# # Base paths
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # 🔥 Use ENV variable (important for Jenkins + backend)
# DATA_DIR = os.getenv("DATA_DIR", os.path.join(BASE_DIR, "data"))
# os.makedirs(DATA_DIR, exist_ok=True)

# print(f"📁 Using DATA_DIR: {DATA_DIR}")

# RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
# PROCESSED_FILE = os.path.join(DATA_DIR, "processed_data.csv")


# def preprocess():
#     print("\n🚀 Preprocessing data...")

#     if not os.path.exists(RAW_FILE):
#         print("❌ raw_data.csv missing")
#         return

#     df = pd.read_csv(RAW_FILE)

#     print(f"📊 Before: {len(df)} rows")

#     # 🔹 Drop null values
#     df.dropna(inplace=True)

#     # 🔹 Remove duplicates (important)
#     df.drop_duplicates(subset=["coin_id", "timestamp"], inplace=True)

#     # 🔹 Convert timestamp
#     df["timestamp"] = pd.to_datetime(df["timestamp"])

#     # 🔹 Sort latest first
#     df.sort_values(by="timestamp", ascending=False, inplace=True)

#     # 🔹 Normalize price (safe)
#     max_price = df["price"].max()
#     if max_price != 0:
#         df["price_normalized"] = df["price"] / max_price
#     else:
#         df["price_normalized"] = df["price"]

#     # 🔹 Price change
#     df["price_change"] = df["price"].diff().fillna(0)

#     # 🔹 Categorize price
#     df["price_category"] = pd.cut(
#         df["price"],
#         bins=3,
#         labels=["Low", "Medium", "High"]
#     )

#     print(f"📉 After: {len(df)} rows")

#     print("📊 Sample processed data:\n", df.head())

#     df.to_csv(PROCESSED_FILE, index=False)

#     print(f"💾 Processed data saved → {PROCESSED_FILE}")


# if __name__ == "__main__":
#     preprocess()

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.getenv("DATA_DIR", os.path.join(BASE_DIR, "data"))
os.makedirs(DATA_DIR, exist_ok=True)

print(f"📁 Using DATA_DIR: {DATA_DIR}")

RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
PROCESSED_FILE = os.path.join(DATA_DIR, "processed_data.csv")


def preprocess():
    print("\n🚀 Preprocessing data...")

    if not os.path.exists(RAW_FILE):
        print("❌ raw_data.csv missing")
        return

    raw_df = pd.read_csv(RAW_FILE)

    print(f"📊 Raw rows: {len(raw_df)}")

    # 🔹 Clean data
    raw_df.dropna(inplace=True)
    raw_df.drop_duplicates(subset=["coin_id", "timestamp"], inplace=True)

    raw_df["timestamp"] = pd.to_datetime(raw_df["timestamp"])

    # 🔹 Feature engineering
    max_price = raw_df["price"].max()
    raw_df["price_normalized"] = raw_df["price"] / max_price if max_price != 0 else raw_df["price"]

    raw_df["price_change"] = raw_df["price"].diff().fillna(0)

    raw_df["price_category"] = pd.cut(
        raw_df["price"],
        bins=3,
        labels=["Low", "Medium", "High"]
    )

    # 🔥 IMPORTANT: APPEND instead of overwrite
    if os.path.exists(PROCESSED_FILE):
        old_df = pd.read_csv(PROCESSED_FILE)

        combined_df = pd.concat([old_df, raw_df], ignore_index=True)

        before = len(combined_df)

        combined_df.drop_duplicates(subset=["coin_id", "timestamp"], inplace=True)

        after = len(combined_df)
        print(f"🧹 Removed duplicates: {before - after}")

    else:
        print("🆕 Creating processed_data.csv")
        combined_df = raw_df

    combined_df.to_csv(PROCESSED_FILE, index=False)

    print(f"💾 Processed rows: {len(combined_df)}")


if __name__ == "__main__":
    preprocess()