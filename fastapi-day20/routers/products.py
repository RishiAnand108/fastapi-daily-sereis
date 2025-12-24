from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import get_session
from models import Product
from schemas import ProductCreate, ProductRead
from auth import get_current_user
from deps import get_product_owned_by_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
    user = Depends(get_current_user)
):
    db_product = Product(
        **product.model_dump(),
        owner_id=user.id
    )
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@router.get("/{product_id}", response_model=ProductRead)
def get_my_product(
    product = Depends(get_product_owned_by_user)
):
    return product
