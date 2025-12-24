from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, products

app = FastAPI(title="Day 20 - Authorization & Permissions")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(products.router)

@app.get("/")
def home():
    return {"message": "Day 20 running"}
