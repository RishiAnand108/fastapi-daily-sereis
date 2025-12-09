import time
from fastapi import Request

async def log_request_info(request: Request, call_next):
    start = time.time()

    #Process request
    response = await call_next(request)

    duration = round(time.time()  - start,4)
    print(f"➡️ {request.method} {request.url.path} took {duration}s")

    #add header
    response.headers['X-Process-Time'] = str(duration)

    return response