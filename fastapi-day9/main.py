# main.py
from fastapi import FastAPI
from database import create_db_and_tables
from routers.users import router as users_router
from routers.orders import router as orders_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users_router)
app.include_router(orders_router)

@app.get("/")
def home():
    return {"message": "Day 9 - Relationships working!"}
