from typing import List
from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: str
    name: str
    category: str
    price: float

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float


class PaginatedResponse(BaseModel):
    total: int
    page: int
    limit: int
    data: List[ProductResponse]    