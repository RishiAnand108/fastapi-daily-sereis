from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from database import get_session
from models import Product
from schemas import PaginatedResponse, ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])   

@router.post('/')
def create_product(
    product: Product,
    session: Session = Depends(get_session)
):
    db_product = Product(**product.model_dump())
    session.add(product)
    session.commit()
    session.refresh(product)
    return db_product

@router.get('/', response_model=PaginatedResponse)
def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=50),
    search: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    sort_by: str | None = None,
    order: str | None = None,
    session: Session = Depends(get_session)
):
    query = select(Product)

    if search:
        query = query.where(Product.name.contains(search))

    if category:
        query = query.where(Product.category == category)   

    if min_price is not None:
        query = query.where(Product.price >= min_price)

    if max_price is not None:
        query = query.where(Product.price <= max_price)

    sort_column = Product.price if sort_by == 'price' else Product.name    
    query = query.order_by(sort_column.desc() if order == 'desc' else sort_column.asc())

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