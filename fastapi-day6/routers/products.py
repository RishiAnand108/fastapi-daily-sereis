from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/api/v1/products",
    tags=['Products']
)

# Request ANd Response MOdel
class Product(BaseModel):
    id: int
    name: str
    price: float

fake_product_db = {}

# CREAte Product
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=Product)
def create_product(product: Product):
    if product.id in fake_product_db:
        raise HTTPException(400, "Product Already Exist")
    
    fake_product_db[product.id] = product
    return product

# gET Product
@router.get('/{product_id}',response_model=Product)
def get_product(product_id: int):
    if product_id not in fake_product_db:
        raise HTTPException(404, "Product not found")
    
    return fake_product_db[product_id]

# GET ALL PRODUCTS
@router.get('/', response_model=List[Product])
def list_products():
    return list(fake_product_db.values())

# DELETE PRODUCT

@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    if product_id not in fake_product_db:
        raise HTTPException(404, "Product not found")
    
    del fake_product_db[product_id]
    return