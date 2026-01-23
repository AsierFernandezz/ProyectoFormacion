from jose import JWTError
from app.repository.user_repo import get_user_by_email, get_user_by_id
from app.core.security import verify_password, create_access_token, decode_access_token


def login_user(email: str, password: str):
    user = get_user_by_email(email)
    if not user:
        raise ValueError("Email y/o contraseña incorrectos")

    if not verify_password(password, user['password']):
        raise ValueError("Email y/o contraseña incorrectos")

    token_data = {"sub": str(user["id"]), "role": user["role"]}
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}

def auth_user(token: str):
    try:
        payload = decode_access_token(token)

        if not payload:
            raise ValueError("Token inválido o expirado")

        user = get_user_by_id(int(payload['sub']))
        print(user)

        if not user:
            raise ValueError("No hay user")

        return user

    except JWTError:
        raise ValueError("Token inválido o expirado 2")
