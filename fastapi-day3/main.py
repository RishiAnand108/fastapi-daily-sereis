from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

app= FastAPI()

class User(BaseModel):
   name: str
   age: Optional[int] = None
   in_stock: bool = True

class Address(BaseModel):
   city: str
   pincode: int   

class Customer(BaseModel):
   name: str
   address: Address #nested model   

@app.post('/users')
def create_user(user: User):
   return {"message":"User received", "data":user}
# ----------------------------------------------------------
# 🔹 TASK 2 — Address Model
# ----------------------------------------------------------
@app.post('/address')
def create_address(address: Address):
   return{
      "message":"Address created",
      "address":address
   }
# ----------------------------------------------------------
# 🔹 TASK 3 — Customer Model (Nested Address)
# ----------------------------------------------------------

print("📌 CUSTOMER endpoint loaded")
@app.post('/customer')
def create_customer(customer: Customer):
   return{
      "message":"Customer Created",
      "customer":customer
   }
print("🟢 Customer route loaded successfully")

# ----------------------------------------------------------
# 🔹 TASK 4 — List of Items (List[BaseModel])
# ----------------------------------------------------------
class Item(BaseModel):
   name: str
   price: float

@app.post('/items')
def create_items(items: List[Item]): 
   return{
      'total_items': len(items),
      'items':items
   } 

# ----------------------------------------------------------
# 🔹 TASK 5 — Order model with List[Item]
# ----------------------------------------------------------

class Order(BaseModel):
   order_id: int
   items: List[Item]

@app.post('/order')
def create_order(order: Order):
   return{
      'message':'order Created',
      'order_id':order.order_id,
      'total_items': len(order.items),
      'items': order.items
         }   

# ----------------------------------------------------------
# 🔹 TASK 6 — Update Customer (Path + Body)
# ----------------------------------------------------------

@app.put('/customer/{customer_id}')
def update_customer(customer_id: int, customer: Customer):
   return {
      'message':'Customer updated',
      'id': customer_id,
      'updated_data': customer
   }

# ----------------------------------------------------------
# 🔹 TASK 6 — Update Customer (Path + Body)
# ----------------------------------------------------------

@app.put('/customer/update/{customer_id}')
def full_update(
   customer_id: int,
   customer: Customer,
   notify: Optional[bool]  = None
):
   return{
      'message':"Full customer update",
      'id': customer_id,
      'customer': customer,
      'notify':notify
   }

# ----------------------------------------------------------
# 🔹 Root Endpoint
# ----------------------------------------------------------

@app.get('/')
def home():
   return {'message':'Day 3 tasks working perfectly'}