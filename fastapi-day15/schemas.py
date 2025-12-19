from typing import List
from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    name:str
    category: str
    price: float

class PaginatedResponse(BaseModel):
    total: int
    page: int
    limit: int
    data: List[ProductResponse]    