import time

_cache = {}

def get_cache(key: str):
    data = _cache.get(key)
    if not data:
        return None
    

    value, expiry = data
    if expiry < time.time():
        del _cache[key]
        return None

    return value

def set_cache(key: str, value, ttl: int = 30):
    expiry = time.time() + ttl
    _cache[key] = (value,expiry) 