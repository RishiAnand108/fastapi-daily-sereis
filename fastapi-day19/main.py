# main.py
# App entry point

from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, products

app = FastAPI(title="FastAPI Day 19 – Relationships")

# Create tables at startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Register routers
app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
def home():
    return {"message": "FastAPI Day 19 running successfully 🚀"}
