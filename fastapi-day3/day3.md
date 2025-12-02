1. Topics Covered

BaseModel

Request Body

Optional Fields

Default Values

Nested Models

Lists of Models

Path + Body

Query + Body

Path + Query + Body

Validation (422 Errors)

2. BaseModel

BaseModel defines the structure and validation rules for JSON request bodies.

Example:

class User(BaseModel):
    name: str
    age: int


If incoming JSON does not match the expected structure or types, FastAPI returns a 422 Unprocessable Entity error.

3. Optional Fields and Default Values

Optional field:

age: Optional[int] = None


Field with default value:

in_stock: bool = True

4. Nested Models

Models can contain other models.

class Address(BaseModel):
    city: str
    pincode: int

class Customer(BaseModel):
    name: str
    address: Address


Example JSON:

{
  "name": "Rishi",
  "address": {
    "city": "Delhi",
    "pincode": 110011
  }
}

5. Lists of Models

Use List[Model] to accept an array of objects.

class Item(BaseModel):
    name: str
    price: float


Example JSON:

[
  {"name": "Pen", "price": 10},
  {"name": "Book", "price": 200}
]

6. Path + Body

Example:

PUT /customer/10


Path gives the ID, and the body contains updated data.

7. Query + Body

Example:

PUT /customer/update/10?notify=true


Query parameters change the behavior of the update request.

8. Complete Day 3 Code
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# 1. User Model — Optional + Default
class User(BaseModel):
    name: str
    age: Optional[int] = None
    in_stock: bool = True

@app.post("/users")
def create_user(user: User):
    return {"message": "User received", "data": user}

# 2. Address Model
class Address(BaseModel):
    city: str
    pincode: int

@app.post("/address")
def create_address(address: Address):
    return {"message": "Address created", "address": address}

# 3. Customer Model (Nested)
class Customer(BaseModel):
    name: str
    address: Address

@app.post("/customer")
def create_customer(customer: Customer):
    return {"message": "Customer created", "customer": customer}

# 4. List Items Example
class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_items(items: List[Item]):
    return {"total_items": len(items), "items": items}

# 5. Order Model (List of Items)
class Order(BaseModel):
    order_id: int
    items: List[Item]

@app.post("/order")
def create_order(order: Order):
    return {
        "message": "Order created",
        "order_id": order.order_id,
        "total_items": len(order.items),
        "items": order.items
    }

# 6. Update Customer (Path + Body)
@app.put("/customer/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    return {"message": "Customer updated", "id": customer_id, "updated_data": customer}

# 7. Full Update (Path + Query + Body)
@app.put("/customer/update/{customer_id}")
def full_update(customer_id: int, customer: Customer, notify: Optional[bool] = None):
    return {"message": "Full customer update", "id": customer_id, "customer": customer, "notify": notify}

@app.get("/")
def home():
    return {"message": "Day 3 Working"}

9. Test JSON Examples
POST /users
{
  "name": "Rishi",
  "age": 20,
  "in_stock": true
}

POST /address
{
  "city": "Delhi",
  "pincode": 110011
}

POST /customer
{
  "name": "Rishi",
  "address": {
    "city": "Delhi",
    "pincode": 110011
  }
}

POST /items
[
  {"name": "Book", "price": 200},
  {"name": "Pen", "price": 20}
]

PUT /customer/10
{
  "name": "Rishi",
  "address": {
    "city": "Mumbai",
    "pincode": 400001
  }
}

PUT /customer/update/10?notify=true
{
  "name": "Rishi",
  "address": {
    "city": "Chennai",
    "pincode": 600001
  }
}

10. Why 422 Errors Happen

A 422 Unprocessable Entity occurs when:

Required fields are missing

Types do not match (e.g., string instead of int)

Nested JSON is incorrect

Lists contain invalid objects

The JSON structure does not match the model

FastAPI performs validation before your function runs.

11. Summary

You learned:

How to design request models

How to validate JSON bodies

How nested models work

How lists of objects work

How path, query, and body combine

How FastAPI returns validation errors

How to build real-world JSON APIs

This completes the foundation required for CRUD operations on Day 4.