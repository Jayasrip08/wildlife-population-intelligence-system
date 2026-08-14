from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Enum, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum
import uuid
from datetime import datetime
from database import Base

class RoleEnum(str, enum.Enum):
    researcher = "researcher"
    officer = "conservation_officer"
    forest_dept = "forest_department"
    admin = "admin"

class ThreatLevelEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.researcher, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    habitat_type = Column(String)
    protected_area = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ImageDetection(Base):
    __tablename__ = "image_detections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    species_detected = Column(String, nullable=False)
    scientific_name = Column(String, nullable=True)
    confidence = Column(Float, nullable=False)
    bounding_box = Column(JSON, nullable=True) # [x_min, y_min, x_max, y_max]
    count = Column(Integer, default=1)
    quality_score = Column(Float, default=0.95)
    behavior = Column(String, nullable=True) # e.g. Grazing, Resting, Alert
    location = Column(String, default="Serengeti Sector 4")
    created_at = Column(DateTime, default=datetime.utcnow)

class AudioDetection(Base):
    __tablename__ = "audio_detections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String, nullable=False)
    species_detected = Column(String, nullable=False)
    scientific_name = Column(String, nullable=True)
    call_type = Column(String, nullable=True) # e.g. Roar, Bird Call, Alarm Call
    confidence = Column(Float, nullable=False)
    spectrogram_url = Column(String, nullable=True)
    duration_seconds = Column(Float, default=5.0)
    frequency_hz = Column(Float, default=2400.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class BiodiversityMetric(Base):
    __tablename__ = "biodiversity_metrics"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    region = Column(String, nullable=False)
    shannon_index = Column(Float, nullable=False) # H' index
    simpson_index = Column(Float, nullable=False) # 1 - D index
    species_richness = Column(Integer, nullable=False) # total unique species
    total_individuals = Column(Integer, nullable=False)
    ecosystem_health_score = Column(Float, nullable=False) # 0 to 100
    habitat_quality_score = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

class WildlifeReport(Base):
    __tablename__ = "wildlife_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    report_type = Column(String, nullable=False) # e.g., Biodiversity Audit, Species Analysis
    summary = Column(Text, nullable=False)
    author = Column(String, nullable=False)
    metrics_json = Column(JSON, nullable=True)
    pdf_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
