from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix='api/v1/users',
    tags=['Users']
)

#Request Model
class User(BaseModel):
    name: str
    email: str

# Response Model (Hides password) 
class UserPublic(BaseModel):
    name: str
    email: str   

fake_users_db = {}

# POST → Register user
@router.post('/',response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register_user(user: User):
    if user.email in fake_users_db:
        raise HTTPException(
            status_code=400,
            detail="User ALready Exists"
        )
    fake_users_db[user.email] = user
    return user

# GET → Fetch user by email
@router.get('/{email}',response_model=UserPublic)
def get_useer(email: str):
     
    if email not in fake_users_db:
        raise HTTPException(404, detail="User not found")
    
    return fake_users_db[email]