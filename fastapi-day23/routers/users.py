from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from database import get_session
from models import User
from schemas import UserCreate, Token
from auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
def register(user: UserCreate, session: Session = Depends(get_session)):
    exists = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if exists:
        raise HTTPException(status_code=400, detail="Email exists")

    db_user = User(
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )
    session.add(db_user)
    session.commit()
    return {"message": "User registered"}

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.email == form_data.username)
    ).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401)

    token = create_access_token({"sub": user.email})
    return {"access_token": token}
