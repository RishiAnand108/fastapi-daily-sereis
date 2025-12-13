from fastapi import FastAPI
from database import create_db_and_tables
from routers.users import router as user_router

app= FastAPI(title="day 8 - postgreSQL integration")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(user_router)  

@app.get("/")
def home():
    return {"message":"Day 8 working with PostgreSQL"}