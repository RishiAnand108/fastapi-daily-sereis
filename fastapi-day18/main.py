from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, products

app = FastAPI(title="FastAPI Day 18 - Relationships")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Day 18 working 🚀"}
