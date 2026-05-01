# # import os
# # import requests
# # import pandas as pd
# # from datetime import datetime

# # # Paths
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # DATA_DIR = os.path.join(BASE_DIR, "data")
# # os.makedirs(DATA_DIR, exist_ok=True)

# # STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")

# # API_KEY = "968d368d8ad6b20fd9dda01ba44f33ab"
# # URL = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}"

# # def fetch_data():
# #     print("\n🚀 Fetching data from API...")

# #     try:
# #         response = requests.get(URL)
# #         data = response.json()

# #         flights = data.get("data", [])
# #         print(f"✅ API Response received: {len(flights)} records")

# #         if not flights:
# #             print("⚠️ No data received from API")
# #             return

# #         processed = []

# #         for flight in flights:
# #             processed.append({
# #                 "flight_iata": flight.get("flight", {}).get("iata"),
# #                 "airline": flight.get("airline", {}).get("name"),
# #                 "departure_airport": flight.get("departure", {}).get("airport"),
# #                 "arrival_airport": flight.get("arrival", {}).get("airport"),
# #                 "status": flight.get("flight_status"),
# #                 "timestamp": datetime.now()
# #             })

# #         df = pd.DataFrame(processed)

# #         print("📊 Sample data:\n", df.head())

# #         df.to_csv(STAGING_FILE, index=False)

# #         print(f"💾 Saved to staging_data.csv ({len(df)} rows)")

# #     except Exception as e:
# #         print("❌ Error fetching data:", e)


# # if __name__ == "__main__":
# #     fetch_data()

# import os
# import requests
# import pandas as pd
# from datetime import datetime

# # Paths
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# os.makedirs(DATA_DIR, exist_ok=True)

# STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")

# # API
# URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=100&page=1"


# def fetch_data():
#     print("\n🚀 Fetching crypto data from CoinGecko...")

#     try:
#         response = requests.get(URL, timeout=10)
#         data = response.json()

#         print(f"✅ API Response received: {len(data)} records")

#         if not data:
#             print("⚠️ No data received")
#             return

#         processed = []

#         for coin in data:
#             processed.append({
#                 "coin_id": coin.get("id"),
#                 "symbol": coin.get("symbol"),
#                 "price": coin.get("current_price"),
#                 "market_cap": coin.get("market_cap"),
#                 "timestamp": datetime.now()
#             })

#         df = pd.DataFrame(processed)

#         print("📊 Sample data:\n", df.head())

#         df.to_csv(STAGING_FILE, index=False)

#         print(f"💾 Saved staging_data.csv ({len(df)} rows)")

#     except Exception as e:
#         print("❌ Fetch error:", e)


# if __name__ == "__main__":
#     fetch_data()


import os
import requests
import pandas as pd
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=100&page=1"


def fetch_data():
    print("\n🚀 Fetching crypto data...")

    try:
        response = requests.get(URL, timeout=10)

        # 🔥 Debug print
        print(f"🔍 Status Code: {response.status_code}")

        data = response.json()

        # 🔥 Check if valid list
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

    except Exception as e:
        print("❌ Fetch error:", e)


if __name__ == "__main__":
    fetch_data()