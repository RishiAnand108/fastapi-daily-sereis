from fastapi import APIRouter, Query
from data import items_db

router = APIRouter(prefix='/items', tags=['Items'])

@router.get('/')
def list_items(
    page: int = Query(1, ge=1),
    limit: int = Query(10, le=50),
    min_price: int | None = None,
    max_price: int | None = None
):
    filtered_items = items_db

    if min_price is not None:
        filtered_items = [i for i in filtered_items if i ['price'] >= min_price]

    if max_price is not None:
        filtered_items = [i for i in filtered_items if i ['price'] <= max_price]

    start = (page - 1) * limit
    end = start + limit

    return{
        "page": page,
        "limit": limit,
        "total": len(filtered_items),
        "items": filtered_items[start:end]
    }   