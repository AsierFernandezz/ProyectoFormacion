from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(String, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)

# Pydantic models
class UserBase(BaseModel):
    username: str
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    role: str
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
        extra = "ignore"
