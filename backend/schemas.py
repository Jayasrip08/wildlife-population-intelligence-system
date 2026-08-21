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

# ================= MILESTONE 3 SCHEMAS =================

class PopulationEstimateRequest(BaseModel):
    species_name: str
    region: str
    observed_count: int
    area_km2: float
    detection_probability: Optional[float] = 0.82

class PopulationEstimateResponse(BaseModel):
    id: UUID
    species_name: str
    region: str
    observed_count: int
    detection_probability: float
    estimated_population: int
    area_km2: float
    density_per_km2: float
    confidence_interval_lower: int
    confidence_interval_upper: int
    growth_rate_pct: float
    created_at: datetime

    class Config:
        from_attributes = True

class HabitatAnalysisRequest(BaseModel):
    region: str
    ndvi_index: float # 0.0 to 1.0
    canopy_cover_pct: float # 0 to 100
    degradation_index: float # 0.0 to 1.0

class HabitatAnalysisResponse(BaseModel):
    id: UUID
    region: str
    ndvi_index: float
    canopy_cover_pct: float
    degradation_index: float
    suitability_score: float
    primary_threat: str
    water_availability_score: float
    created_at: datetime

    class Config:
        from_attributes = True

class HealthScoreInput(BaseModel):
    region: str
    species_diversity: float # 0 to 100
    population_stability: float # 0 to 100
    habitat_quality: float # 0 to 100
    endangered_species_status: float # 0 to 100
    environmental_conditions: float # 0 to 100

class ConservationRecommendationResponse(BaseModel):
    id: UUID
    region: str
    species_diversity_score: float
    population_stability_score: float
    habitat_quality_score: float
    endangered_species_score: float
    environmental_conditions_score: float
    overall_ecosystem_health: float
    health_status: str
    priority_action: str
    patrol_unit_allocation: int
    restoration_corridor_needed: str
    created_at: datetime

    class Config:
        from_attributes = True
