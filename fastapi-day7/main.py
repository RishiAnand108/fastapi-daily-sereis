from fastapi import FastAPI
from middleware import log_request_info
from settings import settings
from routers import search,auth

app = FastAPI(title=settings.APP_NAME)

#add middleware
app.middleware("http")(log_request_info)

#Include routers
app.include_router(search.router)
app.include_router(auth.router)

@app.get('/')
def home():
    return {"message":"DAY 7 Working", "version":settings.API_VERSION}