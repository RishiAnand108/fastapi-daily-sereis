from fastapi import FastAPI
from routers import user, product, order #we('/) hhave to create these next

app=FastAPI()

#include routes
app.include_router(user.router)
app.include_router(product.router)
app.include_router(order.router)

@app.get('/')
def home():
    return {"message":" DAy 5- Routers Working"}

