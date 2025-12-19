from fastapi import FastAPI, Request
from database import create_db_and_tables
from routers.products import router
import time

app=FastAPI(title="Day 15 - Pagination & Middleware")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() -  start
    print(f"{request.method} {request.url.path} - {duration:.4f}s")
    return response

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(router)

@app.get("/")
def home():
    return {"message": " Day 15 API Working"}