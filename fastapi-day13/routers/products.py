from fastapi import APIRouter, Request, Depends
from cache import get_cache, set_cache
from rate_limiter import rate_limit

router = APIRouter(prefix="/products",tags=["Products"])

FAKE_PRODUCTS = [
    {"id":1, "name":"Laptop"},
    {"id":2, "name":"Phone" },
    {"id":3, "name":"Headphones"},
]

@router.get('/')
def list_products(request: Request):
    rate_limit(request)

    cached = get_cache("products")
    if cached:
        return{
            "source":"cache",
            "data":cached
        }
    
    set_cache("products", FAKE_PRODUCTS, ttl=30)

    return {
        "source":"database",
        "data": FAKE_PRODUCTS
    }