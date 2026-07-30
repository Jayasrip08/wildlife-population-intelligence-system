from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional
from models import RoleEnum

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[RoleEnum] = RoleEnum.researcher

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: str
    role: RoleEnum
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class SurveyCreate(BaseModel):
    name: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    habitat_type: Optional[str] = None
    protected_area: Optional[str] = None

class SurveyResponse(SurveyCreate):
    id: UUID
    created_by: UUID
    created_at: datetime
    
    class Config:
        from_attributes = True
