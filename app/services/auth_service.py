from fastapi import Depends
from jose import JWTError
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repository.user_repo import get_user_by_username, get_user_by_id
from app.core.security import verify_password, create_access_token, decode_access_token

def login_user(username: str, password: str, db: Session):
    user = get_user_by_username(db, username)
    if not user:
        raise ValueError("Usuario y/o contraseña incorrectos")

    if not verify_password(password, user.password):
        raise ValueError("Usuario y/o contraseña incorrectos")

    return user

def auth_user(token: str, db: Session):
    try:
        payload = decode_access_token(token)

        if not payload:
            raise ValueError("Token inválido o expirado")

        user = get_user_by_id(db, int(payload['sub']))

        if not user:
            raise ValueError("No hay user")

        return user

    except JWTError:
        raise ValueError("Token inválido o expirado 2")
