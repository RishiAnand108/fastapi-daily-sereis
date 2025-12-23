# schemas.py
# Request & Response schemas (API layer)

from typing import List
from sqlmodel import SQLModel

# ---------- PRODUCT ----------

class ProductCreate(SQLModel):
    name: str
    category: str
    price: float
    owner_id: int

class ProductRead(SQLModel):
    id: int
    name: str
    category: str
    price: float

# ---------- USER ----------

class UserCreate(SQLModel):
    email: str

class UserRead(SQLModel):
    id: int
    email: str
    products: List[ProductRead] = []

