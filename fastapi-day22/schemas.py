from typing import List
from sqlmodel import SQLModel

# -------- USERS --------
class UserCreate(SQLModel):
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    email: str

# -------- AUTH --------
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

# -------- PRODUCTS --------
class ProductCreate(SQLModel):
    name: str
    category: str
    price: float

class ProductRead(SQLModel):
    id: int
    name: str
    category: str
    price: float
