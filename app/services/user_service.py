from typing import List
from fastapi import Depends
from app.db.session import get_db
from app.models import User
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserPublic
from app.models.role import Role
from app.repository.user_repo import get_all_users, get_user_by_username

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user:UserCreate, db: Session = Depends(get_db)) -> UserPublic:
    if get_user_by_username(db, user.username):
        raise ValueError("Este user ya existe")

    # hashear la contraseña
    hashed_password = pwd_context.hash(user.password)

    # crear usuario
    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=Role.USER.value,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return UserPublic.from_orm(new_user)

def get_user(username: str, db: Session = Depends(get_db)) -> UserPublic:
    existing_user = get_user_by_username(db, username)
    print(existing_user)
    if not existing_user:
        raise ValueError(f"No se ha encontrado ningun usuario con el email {username}")
    return UserPublic(
        username=existing_user.username,
        name=existing_user.name,
        email=existing_user.email,
        created_at=existing_user.created_at,
    )
    # Si no encontramos ningún usuario, lanzamos el error

def get_users(db: Session = Depends(get_db)) -> List[UserPublic]:
    return  [
        UserPublic(
            username=user.username,
            name=user.name,
            email=user.email,
            created_at=user.created_at,
        )
        for user in get_all_users(db)
    ]