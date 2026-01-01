from fastapi import FastAPI
from database import create_db_and_tables
from routers import products

app = FastAPI(title="Day 27 - Pagination & Filtering")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(products)

@app.get("/")
def root():
    return {"message": "Day 27 running"}
