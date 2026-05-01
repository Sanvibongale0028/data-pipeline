import os
import requests
import pandas as pd
from datetime import datetime
import time

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔥 Use ENV variable (important for Jenkins)
DATA_DIR = os.getenv("DATA_DIR", os.path.join(BASE_DIR, "data"))
os.makedirs(DATA_DIR, exist_ok=True)

print(f"📁 Using DATA_DIR: {DATA_DIR}")

STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=100&page=1"


def fetch_data(retries=3):
    print("\n🚀 Fetching crypto data...")

    try:
        response = requests.get(URL, timeout=10)

        print(f"🔍 Status Code: {response.status_code}")

        # 🔥 Handle rate limit (429)
        if response.status_code == 429:
            if retries > 0:
                print("⚠️ Rate limit hit → waiting 10 seconds...")
                time.sleep(10)
                return fetch_data(retries - 1)
            else:
                print("❌ Max retries reached. Skipping fetch.")
                return

        data = response.json()

        # 🔥 Validate response
        if not isinstance(data, list):
            print("❌ Unexpected API response:", data)
            return

        print(f"✅ Records received: {len(data)}")

        if not data:
            print("⚠️ No data received")
            return

        processed = []

        for coin in data:
            if not isinstance(coin, dict):
                continue

            processed.append({
                "coin_id": coin.get("id"),
                "symbol": coin.get("symbol"),
                "price": coin.get("current_price"),
                "market_cap": coin.get("market_cap"),
                "timestamp": datetime.now()
            })

        df = pd.DataFrame(processed)

        print("📊 Sample:\n", df.head())

        df.to_csv(STAGING_FILE, index=False)

        print(f"💾 Saved staging_data.csv ({len(df)} rows)")

    except requests.exceptions.RequestException as e:
        print("❌ Network/API error:", e)

    except Exception as e:
        print("❌ Unexpected error:", e)


if __name__ == "__main__":
    fetch_data()