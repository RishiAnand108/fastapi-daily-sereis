# routers/products.py
# Product APIs

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Product, User
from schemas import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["Products"])

# Create product
@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session)
):
    # Check owner exists
    owner = session.get(User, product.owner_id)
    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")

    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        owner_id=product.owner_id
    )

    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return new_product


# List all products
@router.get("/", response_model=list[ProductRead])
def list_products(
    session: Session = Depends(get_session)
):
    products = session.exec(select(Product)).all()
    return products
