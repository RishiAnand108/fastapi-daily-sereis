from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from database import get_session
from models import Product
from schemas import ProductCreate, ProductRead, PaginatedProducts

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductRead)
def create_product(
    product: ProductCreate,
    session: Session = Depends(get_session)
):
    db_product = Product(
        name=product.name,
        category=product.category,
        price=product.price
    )

    session.add(db_product)
    session.commit()
    session.refresh(db_product)

    return db_product

@router.get("/", response_model=PaginatedProducts)
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    search: str | None = None,
    category: str | None = None,
    sort_price: str | None = Query(None, regex="^(asc|desc)$"),
    session: Session = Depends(get_session)
):
    query = select(Product)

    # 🔍 Search by name
    if search:
        query = query.where(Product.name.contains(search))

    # 🏷 Filter by category
    if category:
        query = query.where(Product.category == category)

    # 🔃 Sorting
    if sort_price == "asc":
        query = query.order_by(Product.price.asc())
    elif sort_price == "desc":
        query = query.order_by(Product.price.desc())

    total = len(session.exec(query).all())

    offset = (page - 1) * limit
    products = session.exec(
        query.offset(offset).limit(limit)
    ).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "items": products
    }
