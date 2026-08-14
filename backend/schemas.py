from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional, List, Dict, Any
from models import RoleEnum, ThreatLevelEnum

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

# Milestone 2 Schemas

class ImageAnalysisResponse(BaseModel):
    id: UUID
    filename: str
    species_detected: str
    scientific_name: Optional[str]
    confidence: float
    bounding_box: Optional[List[float]]
    count: int
    quality_score: float
    behavior: Optional[str]
    location: str
    created_at: datetime

    class Config:
        from_attributes = True

class AudioAnalysisResponse(BaseModel):
    id: UUID
    filename: str
    species_detected: str
    scientific_name: Optional[str]
    call_type: Optional[str]
    confidence: float
    duration_seconds: float
    frequency_hz: float
    created_at: datetime

    class Config:
        from_attributes = True

class BiodiversityMetricsResponse(BaseModel):
    id: UUID
    region: str
    shannon_index: float
    simpson_index: float
    species_richness: int
    total_individuals: int
    ecosystem_health_score: float
    habitat_quality_score: float
    timestamp: datetime

    class Config:
        from_attributes = True

class ReportRequest(BaseModel):
    title: str
    region: str
    author: str

class ReportResponse(BaseModel):
    id: UUID
    title: str
    report_type: str
    summary: str
    author: str
    metrics_json: Optional[Dict[str, Any]]
    created_at: datetime

    class Config:
        from_attributes = True
