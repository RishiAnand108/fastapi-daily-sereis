from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from database import get_session
from models import User
from crud import create_user, get_user_by_email
from auth import hash_password

router =  APIRouter(prefix='/users', tags=['Users'])

@router.post("/")
def register_user(user: User, session: Session = Depends(get_session)):
    existing = get_user_by_email(session, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user.hashed_password= hash_password(user.hashed_password)
    return create_user(session, user)

