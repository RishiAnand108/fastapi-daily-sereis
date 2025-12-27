from fastapi import FastAPI
from routers import users, products, admin
from database import create_db_and_tables

app = FastAPI(title="FastAPI Day 23")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(admin.router)

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Day 23!"}