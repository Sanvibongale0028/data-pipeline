from fastapi import APIRouter
from app.services.csv_service import (
    get_raw_data,
    get_processed_data,
    get_summary,
    get_status,
    get_consistency_check,
    get_categorical_encoding,
    get_data_analysis,
    get_data_profile
)

router = APIRouter(prefix="/api", tags=["Data"])


# 🔹 RAW DATA
@router.get("/raw-data")
def raw_data():
    return {
        "status": "success",
        "data": get_raw_data()
    }


# 🔹 PROCESSED DATA
@router.get("/processed-data")
def processed_data():
    return {
        "status": "success",
        "data": get_processed_data()
    }


# 🔹 SUMMARY
@router.get("/summary")
def summary():
    return {
        "status": "success",
        "data": get_summary()
    }


# 🔹 STATUS
@router.get("/status")
def status():
    return {
        "status": "success",
        "data": get_status()
    }
    
# 🔹 CONSISTENCY CHECK
@router.get("/consistency-check")
def consistency_check():
    return {
        "status": "success",
        "data": get_consistency_check()
    }
    
# 🔹 CATEGORICAL ENCODING
@router.get("/categorical-encoding")
def categorical_encoding():
    return {
        "status": "success",
        "data": get_categorical_encoding()
    }
    
@router.get("/analysis")
def data_analysis():
    return {
        "status": "success",
        "data": get_data_analysis()
    }
    
@router.get("/profile")
def data_profile():
    return {
        "status": "success",
        "data": get_data_profile()
    }