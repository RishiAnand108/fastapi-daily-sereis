from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import User
from schemas import UserCreate, UserRead
from fastapi import HTTPException

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):
    db_user = User(email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.id == user_id)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
