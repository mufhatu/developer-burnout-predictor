# 🧠 Developer Burnout Prediction API

This is a simple machine learning service that predicts burnout risk based on developer work habits and experience. The goal was to build something end-to-end — from dataset to a working API that can actually be deployed and used.

It’s built with FastAPI and packaged using Docker so it can run anywhere without setup issues.

-------------------------------------------------------------------------------------------------------------

[![CI](https://github.com/mufhatu/developer-burnout-predictor/actions/workflows/ci.yml/badge.svg)](https://github.com/mufhatu/developer-burnout-predictor/actions/workflows/ci.yml)

-------------------------------------------------------------------------------------------------------------

## 🚀 What it does

The API takes in basic inputs about a developer’s working patterns and returns a predicted burnout level:

- Low
- Medium
- High

It’s meant to show how an ML model can be wrapped in a real service, not just run in a notebook.

--------------------------------------------------------------------------------------------------------------

## 🧱 Project structure

app/
├── main.py        → FastAPI app (routes)
├── model.py       → loads model and handles predictions
├── schemas.py     → request/response validation

data/
└── developer_burnout_dataset_7000.csv

Dockerfile
docker-compose.yml
requirements.txt

---

## ⚙️ Project structure
Python
FastAPI
Scikit-learn
Pandas / NumPy
Uvicorn
Docker

--------------------------------------------------------------------------------------------------------------

📡 API usage

GET /

Request URL : http://localhost:8000/health

Response:

{
  "status": "ok"
}

--------------------------------------------------------------------------------------------------------------

Prediction

POST /predict

Example Request:

{
  "age": 40,
  "experience_years": 3,
  "daily_work_hours": 30,
  "sleep_hours": 7,
  "caffeine_intake": 4,
  "bugs_per_day": 6,
  "commits_per_day": 7,
  "meetings_per_day":7,
  "screen_time": 80,
  "exercise_hours": 5,
  "stress_level": 50
}

Example Response:

{
  "burnout_level": "Medium",
  "confidence": 0.89
}

--------------------------------------------------------------------------------------------------------------

🐳 Running the project

1.	Docker
-	docker-compose up –build
        Then open:
        http://localhost:8000/docs  

2.	Without Docker
-	python -m venv venv
-	venv\Scripts\activate
-	pip install -r requirements.txt
-	uvicorn app.main:app –reload

--------------------------------------------------------------------------------------------------------------

🧠 Why built this way
The focus wasn’t just the model — it was making sure the whole thing behaves like a real service:
•	clear separation between API and model logic 
•	structured inputs using schemas 
•	containerized so it runs the same everywhere 
•	simple enough to extend later (more features, better model, etc.)


📌 What could be improved next
•	Improve model performance with better tuning 
•	Add authentication for API access 
•	Add logging and monitoring 
•	Deploy it to a cloud platform

👤 Author
Built by a Master’s Computer Science student focused on backend systems, machine learning, and DevOps-style workflows.



