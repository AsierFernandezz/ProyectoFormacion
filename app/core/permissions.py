from fastapi import Depends, HTTPException

from app.core.security import get_current_user
from app.models.user import User


def require_user(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="Tienes que iniciar sesión para utilizar este endpoint")

    return current_user

def require_admin(current_user: User = Depends(get_current_user)):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="No tienes permisos para acceder aquí")

    return current_user