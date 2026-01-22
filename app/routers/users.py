from fastapi import APIRouter, HTTPException, Depends
from app.models import UserPublic, UserCreate
from app.services.user_service import create_user, get_user, get_users
from typing import List
from app.core.security import get_current_user

router = APIRouter()

@router.post(
    "/user",
    response_model=UserPublic,
    status_code=201,
    description="Create a new user"
)
def create_a_user(user: UserCreate):
    try:
        return create_user(user)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/user/{email}",
    response_model=UserPublic,
    status_code=200
)
def get_user_by_email(email: str = None, current_user: dict = Depends(get_current_user)):
    try:
        return get_user(email)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/users",
    response_model=List[UserPublic],
    status_code=200,
    description="Get all users",
)
def get_all_users():
    try:
        return get_users()

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/user/{id}", response_model=UserPublic, status_code=200)
def update_user(id, user):
    pass

