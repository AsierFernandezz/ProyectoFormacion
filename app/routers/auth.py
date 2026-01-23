from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.models import UserPublic
from app.schemas.auth import TokenResponse, LoginRequest
from app.services.auth_service import login_user, auth_user
from app.core.security import oauth2_scheme

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    try:
        return login_user(request.email, request.password)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/auth/me", response_model=UserPublic)
def authenticate_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):

    token = credentials.credentials

    try:
        return auth_user(token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
