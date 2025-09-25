Student Stress Detector 🚀

A serverless ML-powered system for detecting high-stress students from IoT mental health data.
This repository contains the solution for **Challenge 2: ML Agentic Engineer** for the Founding Engineer position.
The system ingests IoT mental health data, detects students with stress above a threshold, stores alerts in DynamoDB, and exposes them through an API Gateway.

---

🛠️ Tech Stack
- **AWS SAM** – Serverless Application Model  
- **AWS Lambda** – Python runtime for stress detection, TypeScript runtime for alerts retrieval  
- **AWS API Gateway** – REST endpoints  
- **AWS DynamoDB** – Alert storage  
- **Docker** – Local Lambda and DB emulation  
- **Python 3.11** – ML/heuristic logic

---

📌 Features
- **Python Lambda**: Processes the mental health dataset and detects high-stress cases.
- **TypeScript Lambda**: Fetches high-stress alerts from DynamoDB.
- Serverless architecture deployed with AWS SAM.
- Local development with Docker for PostgreSQL simulation.
- Easily adaptable to Terraform.

---

📊 Architecture Overview
+------------------------+     +----------------------------+
|    API Gateway        |<--->| StressDetector Lambda     |
| POST /process-stress  |     | (Python)                   |
+------------------------+     +----------------------------+
             |
             v
+------------------------+     +----------------------------+
|    API Gateway        |<--->| GetAlertsLambda           |
| GET /alerts           |     | (TypeScript)               |
+------------------------+     +----------------------------+
             |
             v
+------------------------+
| DynamoDB Table        |
| HighStressUsers       |
+------------------------+

---

📦 Prerequisites
- Docker (for local testing)
- AWS CLI
- AWS SAM CLI
- Node.js (v18+)
- Python 3.11

---

🚀 Setup & Run Locally
1. Install Dependencies
   bash
   cd py-lambda
   pip install -r requirements.txt -t .
   cd ../ts-lambda
   npm install
   npx tsc
   cd ..
2. Build the SAM App
   sam build
3. Start Local API
   sam local start-api

--------------------------

🛠 API Endpoints

**POST /process-stress**
Processes the provided dataset (university_mental_health_iot_dataset.csv), detects high-stress cases, and stores alerts in DynamoDB.
Request Example:
{
  "dataset_path": "university_mental_health_iot_dataset.csv"
}

Response Example:
{
  "message": "Stress detection complete. Alerts stored."
}

---

**GET /alerts**
Returns all students flagged with high stress.
Response Example:
[
  {
    "record_id": "intake-file01",
    "mental_health_score": 77,
    "timestamp": "2025-05-22T00:00:00Z"
  }
]

---

📊 Dataset
The dataset used is university_mental_health_iot_dataset.csv, containing IoT signals such as:

  - Heart rate
  - Sleep hours
  - Temperature
  - Other physiological and behavioral features
  
These features are used to infer stress levels for students.

---

📘 Future Improvements
Deploy to AWS using CloudFormation or Terraform.
Add real-time ingestion from IoT sensors.
Improve stress detection with ML models.
Agent logging for autonomous behavior tracking.

---

📌 Author
Tanmayee Kulkarni - GenAI and Cloud Enthusiast
