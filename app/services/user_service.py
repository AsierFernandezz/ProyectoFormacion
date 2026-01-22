from datetime import datetime
from typing import List
from passlib.context import CryptContext
from app.models import UserCreate, UserPublic
from app.repository.user_repo import fake_db, get_user_by_email, get_all_users, add_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user:UserCreate = None) -> UserPublic:
    for existing_user in fake_db:
        if get_user_by_email(user.email):
            raise ValueError("Este email ya existe")

    # hashear la contraseña
    hashed_password = pwd_context.hash(user.password)

    # crear usuario
    new_user = {
        "id": len(get_all_users()) +1,
        "name": user.name,
        "email": user.email,
        "password": hashed_password,
        "created_at": datetime.now()
    }
    added_user = add_user(new_user)
    return UserPublic(id=added_user['id'], name=added_user['name'], email=added_user['email'], created_at=added_user['created_at'])

def get_user(email: str) -> UserPublic:
    existing_user = get_user_by_email(email)
    if not existing_user:
        raise ValueError(f"No se ha encontrado ningun usuario con el email {email}")
    return UserPublic(
        id=existing_user['id'],
        name=existing_user['name'],
        email=existing_user['email'],
        created_at=existing_user['created_at']
    )
    # Si no encontramos ningún usuario, lanzamos el error

def get_users() -> List[UserPublic]:
    return  [
        UserPublic(
            id= user['id'],
            name=user['name'],
            email=user['email'],
            created_at=user['created_at']
        )
        for user in get_all_users()
    ]