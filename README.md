# Wildlife Population Intelligence System — User Guide & System Manual

## 1. Executive Summary & Overview
The **Wildlife Population Intelligence System** is an enterprise AI-powered platform for automated species identification, bioacoustic recognition, abundance estimation, remote sensing habitat evaluation, and multi-tier conservation analytics.

---

## 2. Platform Architecture & Modules
- **Module 1: User Authentication & RBAC**: JWT Bearer Token authorization supporting 4 distinct roles:
  - `researcher`: Image/Audio analytical workflows & biodiversity metrics.
  - `conservation_officer`: Field telemetry, collar tracking, and threat monitoring.
  - `forest_department`: Patrol sector beat planning, corridor connectivity, and fire risk logs.
  - `admin`: User provisioning, performance analytics, and system setting dispatch.
- **Module 3: Species Image Classification & Biometric Re-ID**: Automated YOLOv8/ResNet deep learning inference with deterministic perceptual dHash individual re-identification. Supports high-altitude **Drone Aerial Orthomosaic** multi-object ground grid processing.
- **Module 4: Bioacoustic Recognition Engine**: Spectral Centroid FFT audio processing for birds, mammals, amphibians (`African Bullfrog`, `Common Reed Frog`), insects (`Savannah Bush Cricket`, `Cicada Swarm`), and threat acoustic events (`Gunshots`, `Chainsaws`).
- **Module 5 & 6: Population Estimation & GBIF**: Distance sampling abundance modeling ($N = n/p$), exponential growth trajectory forecasting ($P(t) = P_0 e^{rt}$), and live **GBIF API v1 REST integration**.
- **Module 10: Wildlife Health Scoring**: 5-factor weighted ecosystem health evaluation model.
- **Module 13: Reports & Archive**: Seeded report templates (Survey, Population, Biodiversity, Habitat, Conservation) with PDF, CSV, and Excel TSV downloads.

---

## 3. Getting Started & Running Locally

### Backend Setup (FastAPI)
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup (React / Vite)
```bash
cd frontend
npm install
npm run dev
```

### Docker Production Container Deployment
```bash
docker compose up --build -d
```

---

## 4. Automated Testing & Verification
Execute the system integration and security test suite:
```bash
python test_suite.py
python test_reid.py
python test_gbif.py
```
