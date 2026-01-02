from fastapi import FastAPI
from database import create_db_and_tables
from routers import products

app = FastAPI(title="Day 28 - Async FastAPI")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(products)

@app.get("/")
async def root():
    return {"message": "Day 28 running"}
