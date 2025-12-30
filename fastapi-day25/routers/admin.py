from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from database import get_session
from models import User
from deps import admin_only

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def get_all_users(
    session: Session = Depends(get_session),
    admin=Depends(admin_only)
):
    return session.exec(select(User)).all()
