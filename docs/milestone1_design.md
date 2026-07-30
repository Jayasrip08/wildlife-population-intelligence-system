# Milestone 1: Design Process & Core Setup

## 1. Project Objectives
Build an AI-powered Wildlife Population Intelligence System that uses image recognition, acoustic analysis, computer vision, and machine learning to automatically identify wildlife species, estimate population sizes, monitor biodiversity changes, detect endangered species, and analyze habitat health.

## 2. Biodiversity Monitoring Workflows
*   **Survey Definition:** Researcher/Officer initiates a survey, logging GPS coordinates, habitat type, date, and defining the monitoring devices to be used.
*   **Data Ingestion:**
    *   Camera Trap Images & Drone imagery are uploaded to the system.
    *   Audio recordings from sensors are ingested.
*   **Analysis Workflow:**
    *   The Image Engine processes visual data (YOLOv8/ResNet) to detect and classify species, count animals, and log behavior.
    *   The Audio Engine processes sound (YAMNet/BirdNET) to identify bird and animal calls.
*   **Intelligence Generation:** 
    *   System calculates population density, species richness, biodiversity score.
    *   Ecosystem Health Score is evaluated (Species Diversity, Population Stability, Habitat Quality, Endangered Status, Environmental Conditions).
*   **Actionable Output:** Results surface on dashboards for role-based viewing. Alerts trigger for endangered species detection or habitat degradation.

## 3. System Architecture
*   **Frontend:** React.js + Vanilla CSS. Hosted statically or via Vite.
*   **Backend:** FastAPI (Python). Provides REST API, Handles JWT Auth, interfaces with AI Models.
*   **Databases:** 
    *   **PostgreSQL + PostGIS:** Primary relational database (Users, Surveys, Sites, Role RBAC).
    *   **MongoDB:** Secondary database for high-volume logs, flexible metadata (Sensor Readings, Image/Audio Metadata).
*   **AI Models:** YOLOv8, TensorFlow, PyTorch deployed as independent worker services (to be implemented in future weeks).

## 4. Database Schema (Draft)

### PostgreSQL (Relational Data & GIS)

**Table: users**
*   `id` (UUID, PK)
*   `username` (String, Unique)
*   `email` (String, Unique)
*   `hashed_password` (String)
*   `role` (Enum: Researcher, ConservationOfficer, ForestDept, Admin)
*   `created_at` (Timestamp)

**Table: surveys**
*   `id` (UUID, PK)
*   `name` (String)
*   `created_by` (UUID, FK to users)
*   `start_date` (Date)
*   `end_date` (Date)
*   `habitat_type` (String)
*   `protected_area` (String)

**Table: monitoring_sites**
*   `id` (UUID, PK)
*   `survey_id` (UUID, FK to surveys)
*   `location_name` (String)
*   `coordinates` (Geometry/Point - PostGIS)
*   `device_type` (Enum: CameraTrap, AudioSensor, Drone)
*   `status` (Enum: Active, Inactive)

### MongoDB (Document Data)

**Collection: observations**
*   `_id` (ObjectId)
*   `site_id` (UUID from PostgreSQL)
*   `timestamp` (DateTime)
*   `media_type` (Image / Audio)
*   `media_url` (String - S3 path)
*   `ai_results`: {
        `species_detected`: [ { `species`: String, `confidence`: Float, `bounding_box`: Array } ],
        `animal_count`: Int
    }

**Collection: sensor_logs**
*   `_id` (ObjectId)
*   `site_id` (UUID)
*   `temperature` (Float)
*   `humidity` (Float)
*   `timestamp` (DateTime)
