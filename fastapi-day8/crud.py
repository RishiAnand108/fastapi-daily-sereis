from sqlmodel import Session, select 
from models import User

def create_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user(user_id: int, session: Session):
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).first()

def get_users(session: Session):
    statement = select(User)
    return session.exec(statement).all()

def delete_user(user_id: int , session: Session):
    user= get_user(user_id, session)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False