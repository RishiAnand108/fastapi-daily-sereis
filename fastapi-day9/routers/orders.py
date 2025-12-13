# routers/orders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Order, User
from crud import create_order, get_order, list_orders

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=Order)
def api_create_order(order: Order, session: Session = Depends(get_session)):
    # verify user exists before creating order
    user = session.get(User, order.user_id)
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")
    return create_order(session, order)


@router.get("/", response_model=list[Order])
def api_list_orders(session: Session = Depends(get_session)):
    return list_orders(session)


@router.get("/{order_id}", response_model=Order)
def api_get_order(order_id: int, session: Session = Depends(get_session)):
    order = get_order(session, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
