# routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import User, Order
from crud import create_user, get_user, list_users, list_orders_for_user

router = APIRouter(
    prefix="/users",
      tags=["Users"]
      )


@router.post("/", response_model=User)
def api_create_user(user: User, session: Session = Depends(get_session)):
    return create_user(session, user)


@router.get("/", response_model=list[User])
def api_list_users(session: Session = Depends(get_session)):
    return list_users(session)


@router.get("/{user_id}", response_model=User)
def api_get_user(user_id: int, session: Session = Depends(get_session)):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Eager load orders optionally: SQLModel relationship lazy=selectin will help
    return user


@router.get("/{user_id}/orders", response_model=list[Order])
def api_list_user_orders(user_id: int, session: Session = Depends(get_session)):
    user = get_user(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return list_orders_for_user(session, user_id)
