from datetime import datetime
from typing import List
from app.models import UserCreate, UserPublic
from passlib.context import CryptContext

fake_db: List[dict] = [{"id": 1, "name": "Paco", "email": "paco@gmail.com", "created_at": datetime.now()}]
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
        "password": hashed_password,
        "created_at": datetime.now()
    }
    fake_db.append(new_user)
    return UserPublic(id=user.id, name=user.name, email=user.email, created_at=new_user['created_at'])

def get_user(email: str) -> UserPublic:
    for existing_user in fake_db:
        if existing_user['email'] == email:
            return UserPublic(
                id=existing_user['id'],
                name=existing_user['name'],
                email=existing_user['email'],
                created_at=existing_user['created_at']
            )
    # Si no encontramos ningún usuario, lanzamos el error
    raise ValueError(f"No se ha encontrado ningun usuario con el email {email}")

def get_users() -> List[UserPublic]:
    return  [
        UserPublic(
            id= user['id'],
            name=user['name'],
            email=user['email'],
            created_at=user['created_at']
        )
        for user in fake_db
    ]