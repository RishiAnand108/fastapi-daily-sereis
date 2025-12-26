from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, products, protected

app = FastAPI(title="FastAPI Day 22 - JWT Auth")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users)
app.include_router(products)
app.include_router(protected)

@app.get("/")
def home():
    return {"message": "Day 22 running"}
