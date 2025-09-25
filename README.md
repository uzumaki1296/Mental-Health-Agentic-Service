Student Stress Detector 🚀

A serverless ML-powered system for detecting high-stress students from IoT mental health data.
This project implements Challenge 2 (ML Agentic Engineer) from the take-home test. The system ingests IoT mental health data, detects students with stress above a threshold, stores alerts in DynamoDB, and exposes them through an API Gateway.

📌 Features
Data ingestion from CSV (university_mental_health_iot_dataset.csv).
Stress detection using a lightweight ML/heuristic model.
Alert storage in DynamoDB (HighStressUsers table).
Serverless APIs powered by AWS Lambda & API Gateway:
GET /alerts → fetch all high-stress alerts.
Infrastructure defined with AWS SAM (can be extended with Terraform).

🛠️ Tech Stack
AWS SAM – serverless application model
AWS Lambda – Python runtime
AWS API Gateway – REST endpoints
AWS DynamoDB – alert storage
Docker – local Lambda + DB emulation
Python 3.11 – ML/heuristic logic

⚙️ Prerequisites
Docker (running daemon required for SAM local testing)
AWS CLI
AWS SAM CLI
Python 3.11
Node.js (only if modifying the TypeScript Lambda)

🚀 Setup & Run Locally
1. Install Dependencies
2. Build the SAM App
3. Start local API

API Endpoints
GET /alerts
Returns all students flagged with high stress.

📊 Dataset
The dataset used is university_mental_health_iot_dataset.csv, containing IoT signals (heart rate, sleep hours, temperature, etc.) used to infer stress levels.

📘 Future Improvements
Deploy to AWS (CloudFormation/Terraform).
Add real-time ingestion from IoT sensors.
Improve stress detection with ML models.
Agent logging for autonomous behavior tracking.

