from fastapi import FastAPI

from database import create_db_and_tables
from routers import users
from handlers import (
    user_not_found_handler,
    user_exists_handler
)
from exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)

app = FastAPI(title="FastAPI Day 24")

app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)
app.add_exception_handler(
    UserAlreadyExistsException,
    user_exists_handler
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(users)


@app.get("/")
def home():
    return {"message": "Day 24 running"}
