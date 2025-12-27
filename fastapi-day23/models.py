from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    role: str = Field(default="user") # user|admin

    product: List['Product'] = Relationship(back_populates="owner")

class Product(SQLModel, table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float

    owner_id: int =Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="product")
