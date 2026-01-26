from fastapi import FastAPI
from app.routers import users
import app.routers.auth as auth
app = FastAPI()
app.include_router(users.router, tags=["users"])
app.include_router(auth.router, tags=["auth"])