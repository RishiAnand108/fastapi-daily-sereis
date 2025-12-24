from fastapi import Depends,HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Product
from auth import get_current_user

def get_product_owned_by_user(
        product_id: int,
        session: Session = Depends(get_session),
        user=Depends(get_current_user)
):
    product = session.exec(
        select(Product).where(Product.id == product_id
        )
    ).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found or not owned by user")
    
    if product.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this product")
    
    return product