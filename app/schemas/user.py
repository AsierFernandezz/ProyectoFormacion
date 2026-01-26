from datetime import datetime
from pydantic import BaseModel, ConfigDict

# lo que envia el cliente
class UserCreate(BaseModel):
    username: str
    name: str
    email: str
    password: str

# lo que devuelve la API
class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    name: str
    email: str
    created_at: datetime