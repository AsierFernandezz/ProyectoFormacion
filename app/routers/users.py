from fastapi import APIRouter, HTTPException
from app.models import UserPublic, UserCreate
from app.services.user_service import create_user, get_user, get_users
from typing import List

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
def get_user(email: str):
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