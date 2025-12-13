from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from database import get_session
from crud import get_user_by_email
from auth import verify_password, create_access_token

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm =Depends(),
    session: Session = Depends(get_session)
):
    user = get_user_by_email(session, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub":user.email})
    return {"access_token":token, "token_type":"bearer"}