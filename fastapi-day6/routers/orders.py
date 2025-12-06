from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['Orders']
)

#Models
class Item(BaseModel):
    name: str 
    price: float

class Order(BaseModel):
    order_id: int
    items: List[Item]

fake_orders_db = {}


# Create Order
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_order(order: Order):

    if order.order_id in fake_orders_db:
        raise HTTPException(400, "order already exist")
    
    total=sum(item.price for item in order.items)
    fake_orders_db[order.order_id] = order

    return{
        "message":"Order Created",
        "order_id":order.order_id,
        "total":total,
        "items":order.items
    }


# GET order
@router.get('/{order_id}')
def get_order(order_id: int):

    if order_id not in fake_orders_db:
        raise HTTPException(404, 'Order not found')
    
    order = fake_orders_db[order_id]
    total = sum(item.price for item in order.items)

    return{
        "order_id":order_id,
        "items":order.items,
        "total":total
    }
