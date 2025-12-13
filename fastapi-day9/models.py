from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item_name: str
    quantity: int
    user_id: Optional[int] = Field(foreign_key="user.id")

    # Relationship inside the class
    user: Optional["User"] = Relationship(back_populates="orders")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

    # One user -> many orders
    orders: List[Order] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"lazy": "selectin"}
    )
