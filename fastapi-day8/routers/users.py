from fastapi import APIRouter, Depends, HTTPException
from database import get_session
from sqlmodel import Session
from models import User
from crud import create_user, get_user, get_users, delete_user

router = APIRouter(prefix='/users',tags=['Users'])

@router.post('/')
def create_new_user(user: User, session: Session = Depends(get_session)):
    return create_user(user, session)

@router.get("/{user_id}")
def fetch_user(user_id: int, session: Session = Depends(get_session)):
    user = get_user(user_id, session)
    if not user:
        raise HTTPException(404, 'User not found')
    return user

@router.get("/")
def list_users(session: Session = Depends(get_session)):
    return get_user(session)

@router.delete("/{user_id}")
def remove_user(user_id: int, session: Session = Depends(get_session)):
    if not delete_user(user_id, session):
        raise HTTPException(404, "User not found")
    return {"message":"user deleted"}