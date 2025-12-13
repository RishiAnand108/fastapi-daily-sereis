# crud.py
from sqlmodel import select
from sqlmodel import Session
from models import User, Order

# Users
def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user(session: Session, user_id: int):
    return session.get(User, user_id)

def list_users(session: Session):
    statement = select(User)
    return session.exec(statement).all()

# Orders
def create_order(session: Session, order: Order):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order

def get_order(session: Session, order_id: int):
    return session.get(Order, order_id)

def list_orders(session: Session):
    statement = select(Order)
    return session.exec(statement).all()

def list_orders_for_user(session: Session, user_id: int):
    statement = select(Order).where(Order.user_id == user_id)
    return session.exec(statement).all()
