import pandas as pd
from app.utils.file_utils import (
    get_raw_file,
    get_processed_file,
    file_exists
)


# 🔹 RAW DATA
def get_raw_data(limit=50):
    file_path = get_raw_file()

    if not file_exists(file_path):
        return []

    try:
        df = pd.read_csv(file_path)
        return df.tail(limit).to_dict(orient="records")
    except Exception as e:
        print("❌ Error reading raw data:", e)
        return []


# 🔹 PROCESSED DATA
def get_processed_data(limit=50):
    file_path = get_processed_file()

    if not file_exists(file_path):
        return []

    try:
        df = pd.read_csv(file_path)
        return df.tail(limit).to_dict(orient="records")
    except Exception as e:
        print("❌ Error reading processed data:", e)
        return []


# 🔹 SUMMARY
def get_summary():
    file_path = get_processed_file()

    if not file_exists(file_path):
        return {}

    try:
        df = pd.read_csv(file_path)

        return {
            "total_records": len(df),
            "avg_price": float(df["price"].mean()),
            "max_price": float(df["price"].max()),
            "min_price": float(df["price"].min()),
        }

    except Exception as e:
        print("❌ Error generating summary:", e)
        return {}


# 🔹 STATUS
def get_status():
    return {
        "raw_exists": file_exists(get_raw_file()),
        "processed_exists": file_exists(get_processed_file())
    }