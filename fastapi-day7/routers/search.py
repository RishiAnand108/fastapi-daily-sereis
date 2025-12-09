from fastapi import APIRouter,Query

router = APIRouter(
    prefix='/search',
    tags=['Search']
)

@router.get('/')
def search_items(
    q: str = Query(
        min_length=3,
        max_length=20,
        regex='^[a-zA-Z0-9]+$',
        description="Search query"
    ),
    limit: int = Query(gt=0, lt=50, description="Number of results")

):
    return {"query":q, "limit":limit}