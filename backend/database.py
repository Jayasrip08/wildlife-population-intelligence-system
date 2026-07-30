from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# In a real scenario, this would come from environment variables.
# Using a local PostgreSQL database URL for demonstration.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/wildlife_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
