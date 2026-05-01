import os

# 🔥 Base directory (backend/app/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔥 Use Jenkins workspace if available
DATA_DIR = os.getenv(
    "DATA_DIR",
    os.path.join(BASE_DIR, "..", "..", "data")  # fallback for local
)

# Normalize path
DATA_DIR = os.path.abspath(DATA_DIR)

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# 🔹 File paths
RAW_FILE = os.path.join(DATA_DIR, "raw_data.csv")
PROCESSED_FILE = os.path.join(DATA_DIR, "processed_data.csv")
STAGING_FILE = os.path.join(DATA_DIR, "staging_data.csv")
TRACK_FILE = os.path.join(DATA_DIR, "last_snapshot.json")


def get_data_dir():
    return DATA_DIR


def get_raw_file():
    return RAW_FILE


def get_processed_file():
    return PROCESSED_FILE


def get_staging_file():
    return STAGING_FILE


def get_track_file():
    return TRACK_FILE


def file_exists(file_path):
    return os.path.exists(file_path)