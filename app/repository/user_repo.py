from typing import List, Dict

from fastapi.params import Depends

from app.db.database import get_db
from app.models import User
from sqlalchemy.orm import Session

# fake_db = [
#     {
#         "id": 1,
#         "name": "Asier",
#         "email": "asier@email.com",
#         "password": "$2b$12$...",
#         "role": "user",
#         "created_at": datetime.utcnow(),
#     },
#     {
#         "id": 2,
#         "name": "Paco",
#         "email": "paco@email.com",
#         "password": "$2b$12$zC7F6gDMg..r9rXN4aTBu.nHXYWr/UhiSZikOODcH8S2zUoree/12",
#         "role": "user",
#         "created_at": datetime.utcnow(),
#     },
#     {
#         "id": 3,
#         "name": "Nora",
#         "email": "nora@email.com",
#         "password": "$2y$10$ucFHdCarBdDm0md0K0xg5.ZO5SU8Z3CjZYzSOta7jQ2d352lfE4Ri",
#         "role": "admin",
#         "created_at": datetime.utcnow(),
#     }
# ]

# def add_user(user_dict: Dict) -> Dict:
#     fake_db.append(user_dict)
#     return user_dict

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

