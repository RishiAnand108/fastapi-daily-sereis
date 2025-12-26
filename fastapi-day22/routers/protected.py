from fastapi import APIRouter, Depends
from models import User
from deps import get_current_user

router = APIRouter(prefix="/protected", tags=["Protected"])

@router.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }
