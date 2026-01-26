from fastapi import Depends, HTTPException

from app.core.exceptions.exceptions import UserNotAuthenticated, UserNotAdmin
from app.core.security import get_current_user
from app.models.user import User


def require_user(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise UserNotAuthenticated()

    return current_user

def require_admin(current_user: User = Depends(get_current_user)):

    if current_user.role != "admin":
        raise UserNotAdmin(user_id=current_user.id, username=current_user.username, role=current_user.role)

    return current_user