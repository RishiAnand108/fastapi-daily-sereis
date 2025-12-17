import time
from fastapi import HTTPException, Request

_requests = {}

def rate_limit(request: Request, limit: int=5, window: int = 60):
    ip= request.client.host
    now = time.time()

    history = _requests.get(ip,[])
    history = [t for t in history if now - t < window]

    if len(history ) >= limit:
        raise HTTPException(
            status_code=429,
            detail="too many requests. try again later"
        )
    
    history.append(now)
    _requests[ip] = history