import os
import pandas as pd
import json
import sys

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔥 Use ENV variable (important for Jenkins + backend)
DATA_DIR = os.getenv("DATA_DIR", os.path.join(BASE_DIR, "data"))
os.makedirs(DATA_DIR, exist_ok=True)

print(f"📁 Using DATA_DIR: {DATA_DIR}")

STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")
TRACK_FILE = os.path.join(DATA_DIR, "last_snapshot.json")


def detect_change():
    print("\n🔍 Checking for data changes...")

    if not os.path.exists(STAGING_FILE):
        print("❌ staging_data.csv not found")
        sys.exit(1)

    df = pd.read_csv(STAGING_FILE)

    if df.empty:
        print("😴 No data in staging")
        sys.exit(1)

    df_key = df[["coin_id", "price"]].dropna()
    current_snapshot = df_key.to_dict(orient="records")

    print(f"📊 Current rows: {len(current_snapshot)}")

    # 🔹 First run → always allow pipeline
    if not os.path.exists(TRACK_FILE):
        print("🆕 First run → continue pipeline")
        save_snapshot(current_snapshot)
        sys.exit(0)

    # 🔹 Load previous snapshot safely
    try:
        with open(TRACK_FILE, "r") as f:
            last_snapshot = json.load(f)

        # Validate snapshot format
        if not isinstance(last_snapshot, list):
            raise ValueError("Invalid snapshot format")

    except Exception:
        print("⚠️ Snapshot corrupted → resetting")
        save_snapshot(current_snapshot)
        sys.exit(0)

    # 🔹 Convert to dictionaries
    last_dict = {d["coin_id"]: d["price"] for d in last_snapshot}
    current_dict = {d["coin_id"]: d["price"] for d in current_snapshot}

    changed_coins = 0

    for coin in current_dict:
        if coin in last_dict:
            old_price = last_dict[coin]
            new_price = current_dict[coin]

            # 🔥 More sensitive threshold (important fix)
            if abs(new_price - old_price) / max(old_price, 1) > 0.0001:
                changed_coins += 1
        else:
            changed_coins += 1

    print(f"📈 Coins changed: {changed_coins}")

    # 🔥 Trigger condition
    if changed_coins > 0:
        print("🚀 Change detected → continue pipeline")
        save_snapshot(current_snapshot)
        sys.exit(0)   # SUCCESS → continue pipeline
    else:
        print("😴 No change → stop pipeline")
        sys.exit(1)   # FAIL → stop pipeline


def save_snapshot(data):
    with open(TRACK_FILE, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    detect_change()