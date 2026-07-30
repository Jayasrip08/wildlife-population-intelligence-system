from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, auth, database

# Create tables if they don't exist (In prod use Alembic)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Wildlife Population Intelligence System",
    description="API for the Wildlife Population Intelligence System",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Wildlife Population Intelligence System API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/surveys/", response_model=schemas.SurveyResponse)
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.role_required([models.RoleEnum.researcher, models.RoleEnum.officer, models.RoleEnum.admin]))):
    new_survey = models.Survey(
        name=survey.name,
        created_by=current_user.id,
        start_date=survey.start_date,
        end_date=survey.end_date,
        habitat_type=survey.habitat_type,
        protected_area=survey.protected_area
    )
    db.add(new_survey)
    db.commit()
    db.refresh(new_survey)
    return new_survey

@app.get("/surveys/")
def get_surveys(db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return db.query(models.Survey).all()

@app.post("/ingest/dataset")
def ingest_dataset(dataset_name: str, type: str, current_user: models.User = Depends(auth.role_required([models.RoleEnum.admin, models.RoleEnum.researcher]))):
    # Mock implementation for Milestone 1 task: Integrate wildlife image and audio datasets.
    return {"message": f"Dataset {dataset_name} of type {type} successfully queued for ingestion."}

