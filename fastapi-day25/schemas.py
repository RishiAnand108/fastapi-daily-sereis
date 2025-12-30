
from typing import List
from sqlmodel import SQLModel

class UserCreate(SQLModel):
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    email: str
    role: str

class ProductCreate(SQLModel):
    name: str
    price: float

class ProductRead(SQLModel):
    id: int
    name: str
    price: float

class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"
