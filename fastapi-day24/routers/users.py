from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from database import get_session
from models import User
from schemas import UserCreate, UserRead
from exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    existing = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing:
        raise UserAlreadyExistsException()

    new_user = User(email=user.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = session.get(User, user_id)

    if not user:
        raise UserNotFoundException()

    return user
