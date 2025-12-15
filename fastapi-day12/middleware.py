import time
from fastapi import Request

async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time
    print(f"{request.method} {request.url.path} - {duration:.4f}s")

    return response