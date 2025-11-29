from fastapi import FastAPI, Path, Query
from typing import List
from enum import Enum

app = FastAPI()


# Task 1 — Path Parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


# Task 2 — Path Parameter Validation
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(gt=0, description='ID must be Positive')):
    return {'user_id': user_id}


# Task 3 — Simple Query Parameter
@app.get("/search")
def search(q: str | None = None):
    return {"query": q}


# Task 4 — Combine Path + Query
@app.get("/products/{product_id}")
def product_details(product_id: int, review: str | None = None):
    return {"product_id": product_id, "review": review}


# Task 5 — Query Params with Default Values
@app.get("/filter")
def filter_items(limit: int = 10, sort: str = 'asc'):
    return {'limit': limit, 'sort': sort}


# Task 6 — List Query Parameter
@app.get("/tags")
def get_tags(tag: List[str] = Query(default=[])):
    return {"tags": tag}


# Task 7 — Enum Example
class Category(str, Enum):
    mobile = 'mobile'
    laptop = 'laptop'
    tablet = 'tablet'

@app.get('/category/{category_name}')
def get_category(category_name: Category):
    return {'category': category_name}
