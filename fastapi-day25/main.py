from fastapi import FastAPI
from database import create_db_and_tables
from routers import users, products, admin

app = FastAPI(title="Day 25 - Role Based Access Control")

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(products.router)
app.include_router(admin.router)

@app.get("/")
def home():
    return {"message": "Day 25 Running"}
