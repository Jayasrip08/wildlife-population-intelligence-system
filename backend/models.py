from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
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
