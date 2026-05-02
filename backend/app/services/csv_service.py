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
    
# 🔹 PIPELINE CONSISTENCY CHECK
def get_consistency_check(runs=3):
    file_path = get_processed_file()

    if not file_exists(file_path):
        return []

    results = []

    try:
        for i in range(runs):
            df = pd.read_csv(file_path)

            result = {
                "run": f"Run {i+1}",
                "shape": df.shape,
                "missing_values": int(df.isnull().sum().sum()),
                "mean": float(df.select_dtypes(include='number').mean().mean()),
                "std": float(df.select_dtypes(include='number').std().mean())
            }

            results.append(result)

        return results

    except Exception as e:
        print("❌ Error in consistency check:", e)
        return []
    
# 🔹 CATEGORICAL ENCODING CHECK
def get_categorical_encoding():
    raw_path = get_raw_file()
    processed_path = get_processed_file()

    if not file_exists(raw_path) or not file_exists(processed_path):
        return []

    try:
        df_raw = pd.read_csv(raw_path)
        df_processed = pd.read_csv(processed_path)

        result = []

        for col in df_raw.columns:
            before_dtype = str(df_raw[col].dtype)
            after_dtype = str(df_processed[col].dtype) if col in df_processed.columns else "N/A"

            # Only show categorical columns
            if before_dtype == "object":
                result.append({
                    "column": col,
                    "before": before_dtype,
                    "after": after_dtype
                })

        return result

    except Exception as e:
        print("❌ Error in categorical encoding:", e)
        return []
    
# 🔹 DATA ANALYSIS (Missing, Range, Distribution)
def get_data_analysis():
    raw_path = get_raw_file()
    processed_path = get_processed_file()

    if not file_exists(raw_path) or not file_exists(processed_path):
        return {}

    try:
        df_raw = pd.read_csv(raw_path)
        df_processed = pd.read_csv(processed_path)

        def analyze(df):
            return {
                "missing": df.isnull().sum().to_dict(),
                "range": {
                    col: {
                        "min": float(df[col].min()),
                        "max": float(df[col].max())
                    }
                    for col in df.select_dtypes(include="number").columns
                },
                "distribution": {
                    col: df[col].value_counts().to_dict()
                    for col in df.select_dtypes(include="object").columns
                }
            }

        return {
            "raw": analyze(df_raw),
            "processed": analyze(df_processed)
        }

    except Exception as e:
        print("❌ Error in data analysis:", e)
        return {}
    
# 🔹 DATA PROFILE (Clean version)
def get_data_profile():
    raw_path = get_raw_file()
    processed_path = get_processed_file()

    if not file_exists(raw_path) or not file_exists(processed_path):
        return {}

    def profile(df):
        result = {
            "rows": len(df),
            "columns": len(df.columns),
            "details": []
        }

        for col in df.columns:
            col_data = df[col]

            col_info = {
                "column": col,
                "dtype": str(col_data.dtype),
                "unique": int(col_data.nunique()),
                "missing": int(col_data.isnull().sum())
            }

            # Numeric stats
            if pd.api.types.is_numeric_dtype(col_data):
                col_info.update({
                    "mean": float(col_data.mean()),
                    "median": float(col_data.median()),
                    "min": float(col_data.min()),
                    "max": float(col_data.max())
                })
            else:
                # Categorical stats
                col_info.update({
                    "mode": col_data.mode().iloc[0] if not col_data.mode().empty else None,
                    "top_values": col_data.value_counts().head(5).to_dict()
                })

            result["details"].append(col_info)

        return result

    try:
        df_raw = pd.read_csv(raw_path)
        df_processed = pd.read_csv(processed_path)

        return {
            "raw": profile(df_raw),
            "processed": profile(df_processed)
        }

    except Exception as e:
        print("❌ Error in profiling:", e)
        return {}