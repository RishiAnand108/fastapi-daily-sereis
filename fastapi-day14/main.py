from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, protected

app = FastAPI(title="Day 14 - Mini SaaS Backend")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(protected.router)

@app.get("/")
def home():
    return {"message": "Day 14 Backend Running"}
