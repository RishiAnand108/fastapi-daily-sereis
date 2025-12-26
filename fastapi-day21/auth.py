from fastapi import Depends, HTTPException, Header
from sqlmodel import Session,select
from database import get_session
from models import User

def get_current_user(
        x_user_id: int = Header(..., alias="X-User-ID"),
        session: Session = Depends(get_session)
):
    user = session.exec(
        select(User).where(User.id == x_user_id)
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found ")
    
    return user
