from typing import List
from sqlmodel import SQLModel

class UserCreate(SQLModel):
    email: str
    password: str
    role: str = "user"  # user|admin

class UserRead(SQLModel):
    id: int
    email: str
    role: str

class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

class ProductCreate(SQLModel):
    name: str
    price: float

class ProductRead(SQLModel):
    id: int
    name: str
    price: float
