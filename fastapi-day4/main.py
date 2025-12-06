from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional,List

app=FastAPI()


# ---------------------------
# MODEL
# ---------------------------

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    description: Optional[str] = None

#in-memory database

product_db={ }    # key=product_id, value = Product


# ---------------------------
# CREATE (POST)
# ---------------------------

@app.post('/products')
def create_product(product_id: int, product: Product):
    if product_id in product_db:
        raise HTTPException(status_code=400,detail='Product ID already exists')
    
    product_db[product_id] = product
    return {'messeage':'Product created','id':product_id,'data':product}
# ---------------------------
# READ - GET ALL PRODUCTS
# ---------------------------

@app.get('/products')
def get_all_products():
    return {'count':len(product_db),'products':product_db}

# ---------------------------
# READ - GET SINGLE PRODUCT
# ---------------------------

@app.get('')
def get_product(product_id: int):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail='Product not found')
    
    return product_db[product_id]

# ---------------------------
# UPDATE - ENTIRE PRODUCT (PUT)
# ---------------------------

@app.put('/products/{product_id}')
def update_product(product_id:int, product: Product):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail='Product not found')
    
    product_db[product_id] = product
    return {'message': "product updated", 'updated_data':product}


# ---------------------------
# PARTIAL UPDATE (PATCH)
# ---------------------------

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    in_stock: Optional[bool] = None
    description: Optional[str] = None


@app.patch('/products/{product_id}')
def partial_update(product_id : int, product_data: ProductUpdate):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail='Product not found')

    stored_product= product_db[product_id]

    updated_data = stored_product.model_copy(update=product_data.dict(exclude_unset=True)) 
    product_db[product_id] = updated_data

    return {'message': 'Product partially updated', 'updated_data': updated_data}  


# ---------------------------
# DELETE
# ---------------------------

@app.delete('/products/{product_id}')
def delete_product(product_id: int):
    if product_id not in product_db:
        raise HTTPException(status_code=404, detail='Product not found')
    
    del product_db[product_id]
    return {'message': 'Product deleted successfully','id': product_id}

# Root
@app.get('/')
def home():
    return {'message': 'Welcome to the Product API'}