from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix='/orders', tags=['Orders'])

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    order_id: int
    items: List[Item]

# POST /orders
@router.post('/')
def create_order(order: Order):
    total = sum(item.price for item in order.items)
    return{
        "message":"order Created",
        "order_id": order.order_id,
        'total_amount' : total,
        "items":order.items,
    } 