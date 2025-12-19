from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from settings import settings

oautht2_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

def get_current_user(token: str = Depends(oautht2_scheme)):
    try: 
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )