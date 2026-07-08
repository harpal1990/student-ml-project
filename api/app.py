from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ----------------------------
# Load Model
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "student_model.pkl"

model = joblib.load(MODEL_PATH)

# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI(
    title="Student Score Prediction API",
    version="1.0"
)

# ----------------------------
# Request Schema
# ----------------------------
class Student(BaseModel):
    study_hours: float
    sleep_hours: float
    attendance: float
    previous_marks: float

# ----------------------------
# Home Endpoint
# ----------------------------
@app.get("/")
def home():
    return {
        "message": "Student ML API is running successfully!"
    }

# ----------------------------
# Health Check
# ----------------------------
@app.get("/health")
def health():
    return {
        "status": "UP"
    }

# ----------------------------
# Prediction Endpoint
# ----------------------------
@app.post("/predict")
def predict(student: Student):

    df = pd.DataFrame([student.model_dump()])

    prediction = model.predict(df)

    return {
        "predicted_score": round(float(prediction[0]), 2)
    }