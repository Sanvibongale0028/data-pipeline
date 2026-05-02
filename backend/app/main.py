from fastapi import FastAPI
from app.routes.data_routes import router as data_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Dynamic Data Pipeline API",
    description="Backend for Jenkins-based data pipeline",
    version="1.0.0"
)

# ✅ CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routes
app.include_router(data_router)

@app.get("/")
def home():
    return {
        "message": "🚀 Backend is running",
        "endpoints": [
            "/api/raw-data",
            "/api/processed-data",
            "/api/summary",
            "/api/status",
            "/api/consistency-check",
            "/api/categorical-encoding"
        ]
    }