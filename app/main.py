from fastapi import FastAPI
from schemas import DeveloperMetrics, PredictionResult
from model import predict_burnout

app = FastAPI(title=" Developer Burnout Predictor")

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/predict", response_model=PredictionResult)
def predict(Metrics: DeveloperMetrics):
    return predict_burnout(Metrics)