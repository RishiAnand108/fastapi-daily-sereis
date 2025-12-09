from fastapi import Depends, HTTPException, Header

# Fake auth token for learning
API_TOKEN = "123abc"

def verify_token(token: str = Header(None)):
    if token != API_TOKEN:
        raise HTTPException(status_code=401,detail='Invalid or missing token')
    return True

def get_user_role(role: str = Header(None)):
    if role not in ["admin","user"]:
        raise HTTPException(status_code=403, detail="Invalid role")
    return role