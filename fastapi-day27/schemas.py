from typing import List
from sqlmodel import SQLModel

class ProductCreate(SQLModel):
    name: str
    category: str
    price: float


class ProductRead(SQLModel):
    id: int
    name: str
    category: str
    price: float


class PaginatedProducts(SQLModel):
    total: int
    page: int
    limit: int
    items: List[ProductRead]
