from fastapi import FastAPI
from database import create_db_and_tables
from routers import users

app = FastAPI(title="Day 26 - Refresh Tokens")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(users.router)

@app.get("/")
def home():
    return {"status": "Day 26 running"}
