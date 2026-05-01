from fastapi import FastAPI
from app.routes.data_routes import router as data_router

app = FastAPI(
    title="Dynamic Data Pipeline API",
    description="Backend for Jenkins-based data pipeline",
    version="1.0.0"
)

# 🔹 Include routes
app.include_router(data_router)


# 🔹 Root endpoint
@app.get("/")
def home():
    return {
        "message": "🚀 Backend is running",
        "endpoints": [
            "/api/raw-data",
            "/api/processed-data",
            "/api/summary",
            "/api/status"
        ]
    }