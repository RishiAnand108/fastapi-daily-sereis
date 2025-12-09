from fastapi import APIRouter, Depends
from dependencies import verify_token, get_user_role

router = APIRouter(
    prefix='/auth',
    tags=["Auth"]

)

@router.get('/secure-data')
def secure_data(token_valid: bool = Depends(verify_token)):
    return {'message':"Secure Data acess granted"}

@router.get('/role-data')
def role_based_access(role: str = Depends(get_user_role)):
    return {"message":f"Access granted to role: {role}"}