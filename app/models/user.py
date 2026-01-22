from datetime import datetime
from pydantic import BaseModel

# lo que recibe la API
class UserCreate(BaseModel):
    id: int
    name: str
    email: str
    password: str
  #  is_active: bool
    role: str

# lo que devuelve la API
class UserPublic(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime