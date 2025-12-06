from fastapi import FastAPI
from routers import users,products, orders

app=FastAPI(
    title="Fastapi Day 6",
    description="Learning response models, prefixes, tags, status code.",
    version='1.0.0'
)

#include routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get('/')
def home():
    return {'message':"dAY 6 Working Successfully"}