from fastapi import FastAPI
from app.routers import users
import app.routers.auth as auth
from app.core.exceptions.exception_registry import ExceptionRegistry

app = FastAPI(
    title="FastAPI Backend",
    description="Professional API with structured error handling",
    version="1.0.0"
)

# Register exception handlers automatically
ExceptionRegistry(app)

# Include routers
app.include_router(users.router, tags=["users"])
app.include_router(auth.router, tags=["auth"])
