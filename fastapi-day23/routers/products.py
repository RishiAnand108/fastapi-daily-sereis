from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from database import get_session
from models import Product
from schemas import ProductCreate, ProductRead
from dependencies.auth_deps import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductRead])
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()

# ✅ CREATE PRODUCT (THIS WAS MISSING)
@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session)
):
    db_product = Product(**product.dict())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product