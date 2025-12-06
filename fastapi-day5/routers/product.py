from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/products',tags=['Products'])

class Product(BaseModel):
    name:str
    price: float

# GET /products
@router.get('/')
def get_products():
    return {"message":"List of Products (dummy data)"}

# POST /products
@router.post('/')
def create_product(product: Product):
    return {'message':"Product created",'data':product}    