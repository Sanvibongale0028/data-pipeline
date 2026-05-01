# # import os
# # import pandas as pd

# # # Paths
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # DATA_DIR = os.path.join(BASE_DIR, "data")
# # os.makedirs(DATA_DIR, exist_ok=True)

# # RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
# # PROCESSED_FILE = os.path.join(DATA_DIR, "preprocess_data.csv")

# # def preprocess():
# #     print("\n🚀 Starting preprocessing...")

# #     if not os.path.exists(RAW_FILE):
# #         print("❌ raw_data.csv not found")
# #         return

# #     df = pd.read_csv(RAW_FILE)

# #     before = len(df)
# #     print(f"📊 Raw rows before cleaning: {before}")

# #     # Drop null values
# #     df.dropna(inplace=True)

# #     # Remove duplicates
# #     df.drop_duplicates(inplace=True)

# #     # Encode status
# #     df["status_encoded"] = df["status"].map({
# #         "scheduled": 0,
# #         "active": 1,
# #         "landed": 2,
# #         "cancelled": -1
# #     })

# #     after = len(df)
# #     print(f"📉 Rows after cleaning: {after}")

# #     df.to_csv(PROCESSED_FILE, index=False)

# #     print("💾 Processed data saved successfully")


# # if __name__ == "__main__":
# #     preprocess()

# import os
# import pandas as pd

# # Paths
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# os.makedirs(DATA_DIR, exist_ok=True)

# RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
# PROCESSED_FILE = os.path.join(DATA_DIR, "preprocess_data.csv")


# def preprocess():
#     print("\n🚀 Starting preprocessing...")

#     if not os.path.exists(RAW_FILE):
#         print("❌ raw_data.csv not found")
#         return

#     df = pd.read_csv(RAW_FILE)

#     before = len(df)
#     print(f"📊 Raw rows before cleaning: {before}")

#     # 🔹 Drop null values
#     df.dropna(inplace=True)

#     # 🔹 Remove duplicates (based on coin + timestamp)
#     df.drop_duplicates(subset=["coin_id", "timestamp"], inplace=True)

#     # 🔹 Convert timestamp to datetime
#     df["timestamp"] = pd.to_datetime(df["timestamp"])

#     # 🔹 Sort by latest data
#     df.sort_values(by="timestamp", ascending=False, inplace=True)

#     # 🔹 Normalize price (0–1 scale)
#     if df["price"].max() != 0:
#         df["price_normalized"] = df["price"] / df["price"].max()
#     else:
#         df["price_normalized"] = df["price"]

#     # 🔹 Price change feature (difference)
#     df["price_change"] = df["price"].diff().fillna(0)

#     # 🔹 Optional: categorize price level
#     df["price_category"] = pd.cut(
#         df["price"],
#         bins=3,
#         labels=["Low", "Medium", "High"]
#     )

#     after = len(df)
#     print(f"📉 Rows after cleaning: {after}")

#     print("📊 Processed sample:\n", df.head())

#     df.to_csv(PROCESSED_FILE, index=False)

#     print("💾 Processed data saved successfully")


# if __name__ == "__main__":
#     preprocess()

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
PROCESSED_FILE = os.path.join(DATA_DIR, "processed_data.csv")


def preprocess():
    print("\n🚀 Preprocessing data...")

    if not os.path.exists(RAW_FILE):
        print("❌ raw_data.csv missing")
        return

    df = pd.read_csv(RAW_FILE)

    print(f"📊 Before: {len(df)} rows")

    df.dropna(inplace=True)
    df.drop_duplicates(subset=["coin_id", "timestamp"], inplace=True)

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.sort_values(by="timestamp", ascending=False, inplace=True)

    df["price_normalized"] = df["price"] / df["price"].max()
    df["price_change"] = df["price"].diff().fillna(0)

    df["price_category"] = pd.cut(
        df["price"],
        bins=3,
        labels=["Low", "Medium", "High"]
    )

    print(f"📉 After: {len(df)} rows")

    df.to_csv(PROCESSED_FILE, index=False)
    print("💾 Processed data saved")


if __name__ == "__main__":
    preprocess()