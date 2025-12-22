from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Product
from schemas import ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session)
):
    db_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,

        owner_id=product.owner_id
    )
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product
