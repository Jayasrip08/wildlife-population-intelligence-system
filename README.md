# 🌿 Wildlife Population Intelligence System — User Guide & System Manual

## 1. Executive Summary & Overview
The **Wildlife Population Intelligence System** is an enterprise AI-powered platform designed for automated species identification, bioacoustic recognition, biometric individual re-identification (Re-ID), abundance estimation, remote sensing habitat evaluation, and live biodiversity telemetry integration.

---

## 2. Platform Architecture & Key Features
- **User Authentication & RBAC**: JWT Bearer Token authorization supporting Role-Based Access Control (`researcher`, `conservation_officer`, `forest_department`, `admin`).
- **Species Image Classification & Biometric Re-ID**: Automated deep learning inference (ResNet18 / YOLOv8 architecture) with perceptual coat pattern frequency quantization for individual animal Re-ID (`IND-***-****`). Supports both stationary camera traps and high-altitude **Drone Aerial Orthomosaic** imagery.
- **Bioacoustic Recognition Engine**: Fast Fourier Transform (FFT) spectral analysis for bioacoustic signals (mammals, birds, amphibians, insects) and anthropogenic threat sounds (chainsaws, gunshots).
- **Population Estimation & Live GBIF API**: Distance sampling abundance modeling ($N = n/p$), exponential trajectory forecasting ($P(t) = P_0 e^{rt}$), and live REST integration with **GBIF (Global Biodiversity Information Facility)**.
- **Wildlife Ecosystem Health Scoring**: 5-factor weighted ecosystem health evaluation model.
- **Automated Report Generation**: Comprehensive PDF, CSV, and Excel reporting for biodiversity surveys, population trends, and conservation alerts.

---

## 3. Tech Stack & Environment Setup

### Tech Stack
- **Backend**: FastAPI (Python 3.10), SQLAlchemy 2.0, PostgreSQL / SQLite, PyTorch, Pillow, Pydantic v2
- **Frontend**: React 19, Vite 8, Tailwind CSS, Lucide Icons
- **Deployment**: Render Blueprint (`render.yaml`), Docker containerization

---

## 4. Local Development Setup

### Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
- API Interactive Swagger UI: `http://localhost:8000/docs`
- Health Endpoint: `http://localhost:8000/health`

### Frontend Setup (React / Vite)
```bash
cd frontend
npm install
npm run dev
```
- Frontend Web App: `http://localhost:5173`

### Multi-Container Local Setup (Docker Compose)
```bash
docker compose up --build -d
```

---

## 5. Automated Verification & Testing
To execute all 3 verification test suites (Biometric Re-ID, Deep Security & JWT Lifecycle, Live GBIF API & Core Metrics):

```bash
python run_all_tests.py
```

---

## 6. Cloud Deployment Guide (Render Blueprint)
This application is pre-configured for automated deployment on **Render** using Blueprint orchestration (`render.yaml`).

### Deployment Steps:
1. Connect your GitHub repository (`Jayasrip08/wildlife-population-intelligence-system`) to Render.
2. Create a **New Blueprint** and select `render.yaml`.
3. Render automatically provisions:
   - 🗄️ **`wildlife-db`**: Managed PostgreSQL database.
   - ⚙️ **`wildlife-backend`**: Dockerized FastAPI Web Service (with dynamic `$PORT` binding and SQLAlchemy database migration).
   - 🎨 **`wildlife-frontend`**: Dockerized React + Nginx Web Service (configured with `VITE_API_URL` pointing to backend host).

---

## 7. License & Compliance
Developed for Wildlife Population Intelligence & Conservation Management.
