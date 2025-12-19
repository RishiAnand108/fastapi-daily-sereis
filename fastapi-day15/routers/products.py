from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from database import get_session
from models import Product
from schemas import PaginatedResponse

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/", response_model=PaginatedResponse)
def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=50),
    search: str | None = None,
    session: Session = Depends(get_session),
):
    query = select(Product)

    if search:
        query = query.where(Product.name.contains(search))

    # These lines MUST be outside the if-block
    total = len(session.exec(query).all())
    offset = (page - 1) * limit

    items = session.exec(
        query.offset(offset).limit(limit)
    ).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": items,
    }
