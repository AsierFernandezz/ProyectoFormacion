from fastapi import FastAPI
from app.core.exceptions.exceptions import UserNotFound, UserAlreadyExists
from app.core.exceptions.exception_handler import (
    user_not_found_handler,
    user_already_exists_handler
)

# Este componente es el que organiza cada qeuja a que hanlder va dirigido

class ExceptionRegistry:
    """Centralized exception handler registration"""

    def __init__(self, app: FastAPI):
        self.app = app
        self._register_handlers()

    def _register_handlers(self):
        """Register all exception handlers"""
        self.app.add_exception_handler(UserNotFound, user_not_found_handler)
        self.app.add_exception_handler(UserAlreadyExists, user_already_exists_handler)

        # Add more handlers as needed
        # self.app.add_exception_handler(DatabaseError, database_handler)
        # self.app.add_exception_handler(AuthError, auth_handler)
