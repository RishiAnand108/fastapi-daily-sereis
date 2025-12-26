from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str

    products: List["Product"] = Relationship(back_populates="owner")

class Product(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: str
    price: float

    owner_id:Optional[int] = Field(foreign_key="user.id")
    owner: Optional[User] = Relationship(back_populates="products")   