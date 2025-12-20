from fastapi import FastAPI, Request
from database import create_db_and_tables
from routers import products
import time

app = FastAPI(title="Day 15 - Pagination & Middleware")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    print(f"{request.method} {request.url.path} - {duration:.4f}s")
    return response

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(products.router)

@app.get("/")
def home():
    return {"message": "Day 15 API running successfully"}
