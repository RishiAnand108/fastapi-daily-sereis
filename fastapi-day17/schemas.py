from typing import List
from pydantic import BaseModel
from models import Product

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float

class PaginatedResponse(BaseModel):
    total: int
    page: int
    limit: int
    data: List[Product]

