from datetime import datetime
from pydantic import BaseModel

# lo que envia el cliente
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# lo que devuelve la API
class UserPublic(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime