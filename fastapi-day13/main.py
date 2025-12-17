from fastapi import FastAPI
from routers import products

app = FastAPI(title="Day 13 - Caching & Rate Limiting")

app.include_router(products.router)

@app.get("/")
def home():
    return {"message": "Day 13 API Running"}
