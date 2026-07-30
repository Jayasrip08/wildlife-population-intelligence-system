# 🐾 AI Wildlife Population Intelligence System

An AI-powered, multi-modal Wildlife Population Intelligence Platform designed for wildlife researchers, conservation officers, forest department personnel, and environmental agencies. The platform leverages Computer Vision (CV), Bioacoustics processing, satellite data, and machine learning models to automatically classify species, estimate animal populations, monitor habitat health, and detect endangered species in real-time.

---

## 📌 Executive Summary & Objectives

The primary goal of the **Wildlife Population Intelligence System** is to automate and scale ecological monitoring using modern AI/ML technologies.

### Key Objectives:
- **Species Identification:** Automated identification of animal species using camera trap images, drone footage, and bioacoustic recordings.
- **Population Estimation:** Counting individuals, calculating density, analyzing migration patterns, and tracking population trends.
- **Habitat Intelligence:** Assessing ecosystem health, vegetation indices (NDVI), and biodiversity richness.
- **Threat Detection & Alerts:** Identifying endangered species, detecting unauthorized human activities/poaching threats, and triggering automated alerts.
- **Role-Based Workflows:** Providing tailored dashboards and permissions for Wildlife Researchers, Conservation Officers, Forest Department Personnel, and System Administrators.

---

## 🏛 System Architecture Overview

```
                          ┌────────────────────────┐
                          │   Frontend Interface   │
                          │ React + Vanilla CSS + Vite│
                          └───────────┬────────────┘
                                      │ REST API / WebSocket
                                      ▼
                          ┌────────────────────────┐
                          │     Backend Core       │
                          │   FastAPI + Python     │
                          └─────┬────────────┬─────┘
                                │            │
           ┌────────────────────┘            └────────────────────┐
           ▼                                                      ▼
┌───────────────────────┐                                ┌─────────────────┐
│ PostgreSQL Database   │                                │  AI Engine      │
│ (Users, Surveys, Logs)│                                │  (PyTorch/YOLO) │
└───────────────────────┘                                └─────────────────┘
```

---

## 🧩 Core Modules & Capabilities

### 1. User Authentication & Role-Based Access Control (RBAC)
- **Authentication:** JWT (JSON Web Tokens) with Access & Refresh Token security mechanics.
- **Roles:**
  - `Wildlife Researcher`: Full access to dataset ingestion, model training, population models, and analytical tools.
  - `Conservation Officer`: Field survey oversight, alert management, and conservation reporting.
  - `Forest Department Officer`: Protected area monitoring, real-time alert reception, and site management.
  - `Administrator`: User management, system health metrics, dataset approvals, and access control.

### 2. Wildlife Survey & Monitoring Management
- Survey lifecycle management (planning, execution, archiving).
- Deployment management for Camera Traps, Bioacoustic Audio Sensors, and Drone paths.
- Metadata tagging (GPS coordinates, habitat type, timestamp, protected area mapping).

### 3. Wildlife Image & Bioacoustic Analysis Engine
- **Camera Trap & Drone Vision:** Animal detection, species classification, bounding box detection, and behavior analysis.
- **Bioacoustic Engine:** Audio spectrum preprocessing, bird call classification, mammal vocalization identification, and background noise filtering.
- **Dataset Ingestion:** Seamless integration with iNaturalist and GBIF (Global Biodiversity Information Facility) data streams.

### 4. Population Estimation & Biodiversity Analytics
- Density and population size estimation algorithms.
- Migration pattern mapping and habitat utilization heatmaps.
- Biodiversity index metrics (Shannon Wiener Index, Species Richness).

---

## 🔐 Environment Setup (`.env`)

The project uses `.env` files for managing local environment configuration, database credentials, and security secrets.

### `.env.example` Template:

```env
# Application Settings
ENV=development
PORT=8000

# Database Credentials
DB_HOST=localhost
DB_PORT=5432
DB_NAME=wildlife_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DATABASE_URL=postgresql://your_db_user:your_db_password@localhost:5432/wildlife_db

# JWT & Authentication Secrets
JWT_SECRET_KEY=your_jwt_secret_key
JWT_REFRESH_SECRET_KEY=your_jwt_refresh_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Default Administrator Account Credentials
ADMIN_DEFAULT_USERNAME=admin
ADMIN_DEFAULT_EMAIL=admin@wildlife-intel.org
ADMIN_DEFAULT_PASSWORD=your_admin_password

# Dataset & Model Paths
DATASET_STORAGE_PATH=./datasets
MODELS_STORAGE_PATH=./models
```

> 🔒 **Security Warning:** Real passwords and secret keys are securely stored in your local `.env` file and excluded from public version control. Never include actual production credentials in documentation or commit `.env` files to git repositories.

---

## 🚀 Getting Started & Installation

### Prerequisites
- **Python:** 3.10 or higher
- **Node.js:** v18 or higher
- **PostgreSQL:** 14 or higher (or SQLite for quick local demo)

### Backend Setup (FastAPI)
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the backend API server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
5. Access interactive API documentation at: `http://localhost:8000/docs`

### Frontend Setup (React + Vite)
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install npm dependencies:
   ```bash
   npm install
   ```
3. Launch the development server:
   ```bash
   npm run dev
   ```

### Frontend Tech Stack & Design System
- **Framework:** React 19 + Vite 8
- **Styling:** Vanilla CSS / Custom CSS with CSS Custom Properties (`:root` variables)
- **Theme:** Adaptive Light & Dark theme supporting `prefers-color-scheme`
- **Responsive Layout:** Flexbox & CSS Grid

---

## 📄 License & Attribution

This project is built based on the specifications outlined in the **AI Wildlife Population Intelligence System Specification PDF**. Designed for wildlife conservation, ecological research, and environmental protection initiatives.
