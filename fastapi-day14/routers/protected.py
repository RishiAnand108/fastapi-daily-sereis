from fastapi import APIRouter, Depends
from dependencies import get_current_user

router = APIRouter(prefix="/protected", tags=["Protected"])

@router.get("/")
def protected_route(user=Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user": user
    }
