from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas import UserPublic, UserCreate
from app.repository.user_repo import get_user_by_id, delete_user_by_id
from app.services.user_service import create_user, get_user, get_users
from typing import List
from app.core.security import get_current_user
from app.models.role import Role

router = APIRouter()

@router.post(
    "/user",
    response_model=UserPublic,
    status_code=201,
    description="Create a new user"
)
def create_a_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(user ,db)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/user/{username}",
    response_model=UserPublic,
    status_code=200
)
def get_user_by_username(current_user: dict = Depends(get_current_user) ,username: str = None, db: Session = Depends(get_db)):

    if current_user.get("role") is None:
        raise HTTPException(status_code=403, detail="Tienes que iniciar sesión para utilizar este endpoint")

    try:
        return get_user(username, db)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get(
    "/users",
    response_model=List[UserPublic],
    status_code=200,
    description="Get all users",
)
def get_all_users(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    try:
        if current_user.get("role") != Role.ADMIN.value:
             raise HTTPException(status_code=403, detail="No tienes permisos para ver todos los usuarios")

        return get_users(db)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/user/{id}", response_model=UserPublic, status_code=200)
def update_user(id, user):
    pass

@router.delete("/user/delete/{id}", status_code=200, description="Delete a user", response_model=dict)
def delete_user(current_user: dict = Depends(get_current_user), id: int = None, db: Session = Depends(get_db)):
    try:
        if current_user.get("role") != Role.ADMIN.value:
            raise HTTPException(status_code=403, detail="No tienes permisos para eliminar un usuario")

        if id is None:
            raise HTTPException(status_code=400, detail="No se ha proporcionado un id")

        user = get_user_by_id(db, id)
        if not user:
            raise HTTPException(status_code=404, detail="No se ha encontrado ningun usuario con el id proporcionado")

        delete_user_by_id(db, id)
        return {"message": "Usuario eliminado correctamente", "user": user.username}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

