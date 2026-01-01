from sqlmodel import SQLModel

class UserCreate(SQLModel):
    email: str
    password: str

class TokenPair(SQLModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshToken(SQLModel):
    refresh_token: str


