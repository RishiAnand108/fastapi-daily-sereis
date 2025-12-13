from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, auth

app = FastAPI(title="day10 - Authentication with JWT")

@app.on_event("startup")
def on_startup():
    create_db_and_tables

app.include_router(users.router)
app.include_router(auth.router) 

@app.get("/")
def home():
    return {"message":"Day 10 JWT AuthWorking"}