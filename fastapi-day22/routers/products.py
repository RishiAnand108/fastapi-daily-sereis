from fastapi import APIRouter, Depends
from sqlmodel import Session

from database import get_session
from models import Product, User
from schemas import ProductCreate, ProductRead
from deps import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        owner_id=current_user.id
    )

    session.add(new_product)
    session.commit()
    session.refresh(new_product)

    return new_product
