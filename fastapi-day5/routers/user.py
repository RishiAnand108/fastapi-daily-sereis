from fastapi import APIRouter
from pydantic import BaseModel

router= APIRouter(prefix='/users',tags=['Users'])

class User(BaseModel):
    name: str
    age: int


#GET / Users 
@router.post('/')
def create_user(user: User):
    return {'message':'User Created', 'data':user}

