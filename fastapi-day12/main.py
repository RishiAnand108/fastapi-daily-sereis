from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middleware import log_requests
from routers import items

app= FastAPI(title="Day 12 - Middleware, CORS & Pagination")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Custom Middleware
app.middleware("http")(log_requests)

# Routers
app.include_router(items.router)

@app.get("/")
def home():
    return {"message": "Day 12 API Running"}
