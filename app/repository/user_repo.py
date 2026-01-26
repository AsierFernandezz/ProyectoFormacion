from typing import List, Dict

from fastapi.params import Depends

from app.db.database import get_db
from app.models import User
from sqlalchemy.orm import Session

# En user_repo.py
def get_all_users(db: Session) -> List[User]:
    users = db.query(User).all()
    print("Usuarios en la base de datos:")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    return users

def get_user_by_username(db: Session = Depends(get_db), username: str = None) -> User | None:
    print(username, User.username)
    user = db.query(User).filter( User.username == username).first()
    print(f"User: {user}")
    return user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def delete_user_by_id(db: Session, user_id: int) -> None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

