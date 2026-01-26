from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions.exceptions import UserNotFound, UserAlreadyExists
import logging

logger = logging.getLogger(__name__)

# Este componente es el que recibe la queja y la traduce al cliente a un formato JSON


class BaseExceptionHandler:
    """Base class for exception handlers"""

    @staticmethod
    def create_response(
            status_code: int,
            detail: str,
            error_code: str = None,
            extra_data: dict = None
    ) -> JSONResponse:
        content = {"detail": detail}
        if error_code:
            content["error_code"] = error_code
        if extra_data:
            content.update(extra_data)

        return JSONResponse(status_code=status_code, content=content)


class UserExceptionHandler(BaseExceptionHandler):
    """Handle user-related exceptions"""

    @staticmethod
    async def user_not_found(request: Request, exc: UserNotFound) -> JSONResponse:
        logger.warning(f"User not found: {exc.username}")

        return UserExceptionHandler.create_response(
            status_code=404,
            detail="User not found",
            error_code="USER_NOT_FOUND",
            extra_data={
                "user_id": exc.user_id,
                "username": exc.username
            }
        )

    @staticmethod
    async def user_already_exists(request: Request, exc: UserAlreadyExists) -> JSONResponse:
        logger.warning(f"User already exists: {exc.username}")

        return UserExceptionHandler.create_response(
            status_code=409,
            detail="User already exists",
            error_code="USER_ALREADY_EXISTS",
            extra_data={
                "user_id": exc.user_id,
                "username": exc.username
            }
        )


# Export handlers for registration
user_not_found_handler = UserExceptionHandler.user_not_found
user_already_exists_handler = UserExceptionHandler.user_already_exists
