from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions import UserNotFoundException, UserAlreadyExistsException

def user_not_found_handler(
        request: Request,
        exc: UserNotFoundException

):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": "USER_NOT_FOUND",
            "message_code": "USER does not exist"
        }
    )

def user_exists_handler(
        request: Request,
        exc: UserAlreadyExistsException

):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": "USER_ALREADY_EXISTS",
            "message_code": "USER with given email already exists"
        }
)