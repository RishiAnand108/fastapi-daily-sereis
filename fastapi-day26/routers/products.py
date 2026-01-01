from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session
from models import Product, User
from schemas import ProductCreate, ProductRead
from deps import get_current_user

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session),
    current_user: str = Depends(get_current_user)
):
    user = session.exec(
        select(User).where(User.email == current_user)
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    db_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        owner_id=user.id
    )

    session.add(db_product)
    session.commit()
    session.refresh(db_product)

    return db_product

@router.get("/", response_model=list[ProductRead])
def list_products(session: Session = Depends(get_session)):
    return session.exec(select(Product)).all()
