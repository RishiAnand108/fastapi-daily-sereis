from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.customs import UserNotFoundError, ProductNotFoundError

async def user_not_found_handler(
        request: Request,
        exc: UserNotFoundError
):
    
    return JSONResponse(
        status_code=404,
        content={
           "error":"User Not Found",
           "user_id": exc.user_id
        }
    )

async def product_not_found_handler(
        request: Request,
        exc: ProductNotFoundError
):
    return JSONResponse(
        status_code=404,
        content={
           "error":"Product Not Found",
           "product_id": exc.product_id
        }
    )   