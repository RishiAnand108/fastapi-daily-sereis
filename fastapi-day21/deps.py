from fastapi import Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import Product
from auth import get_current_user

def get_product_owned_by_user(
    product_id: int,
    session: Session = Depends(get_session),
    user = Depends(get_current_user)
):
    product = session.get(Product, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.owner_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    return product
