from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import User
from schemas import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
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
        raise HTTPException(status_code=404, detail="User not found")
    return user
