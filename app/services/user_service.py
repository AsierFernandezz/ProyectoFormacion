from datetime import datetime
from typing import List
from app.models import UserCreate, UserPublic
from passlib.context import CryptContext

fake_db: List[dict] = []
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user:UserCreate = None) -> UserPublic:
    for existing_user in fake_db:
        if existing_user['email'] == user.email:
            raise ValueError("Este email ya existe")

    # hashear la contraseña
    hashed_password = pwd_context.hash(user.password)

    # crear usuario
    new_user = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }
    fake_db.append(new_user)
    return UserPublic(id=user.id, name=user.name, email=user.email, created_at=datetime.now())

user1 = UserCreate(id=1, name="Paco", email="paco@gmail.com", password="locowin")

create_user(user1)