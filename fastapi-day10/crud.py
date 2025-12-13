from sqlmodel import Session, select
from models import User

def get_user_by_email(session: Session, email: str):
    statement=select(User).where(User.email == email)
    return session.exec(statement).first()

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user