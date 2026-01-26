from jose import JWTError
from sqlalchemy.orm import Session
from app.core.exceptions.exceptions import TokenExpired, UserNotFound
from app.repository.user_repo import get_user_by_username, get_user_by_id
from app.core.security import verify_password, decode_access_token

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
            raise TokenExpired

        user = get_user_by_id(db, int(payload['sub']))

        if not user:
            raise UserNotFound(username=user.username)

        return user

    except JWTError:
        raise TokenExpired
