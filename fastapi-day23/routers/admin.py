from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models import Product
from schemas import ProductCreate
from dependencies.auth_deps import admin_only

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/products")
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
    admin=Depends(admin_only)
):
    db_product = Product(
        name=product.name,
        price=product.price,
        owner_id=admin.id
    )
    session.add(db_product)
    session.commit()
    return db_product
