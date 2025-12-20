from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from database import get_session
from models import Product
from schemas import PaginatedResponse, ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=PaginatedResponse)
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=50),
    search: str | None = None,
    session: Session = Depends(get_session)
):
    query = select(Product)

    if search:
        query = query.where(Product.name.contains(search))

    all_items = session.exec(query).all()
    total = len(all_items)

    offset = (page - 1) * limit
    products = session.exec(
        query.offset(offset).limit(limit)
    ).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": products
    }

@router.post("/", response_model=Product)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session)
):
    db_product = Product(**product.model_dump())
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product