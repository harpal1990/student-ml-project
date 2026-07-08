from pathlib import Path
import pandas as pd
import joblib

from utils import load_config

BASE_DIR = Path(__file__).resolve().parent.parent

config = load_config()

MODEL_PATH = BASE_DIR / config["paths"]["model"]

model = joblib.load(MODEL_PATH)

student = pd.DataFrame([
    {
        "study_hours": 8,
        "sleep_hours": 6,
        "attendance": 80,
        "previous_marks": 70
    }
])

prediction = model.predict(student)

print(
    f"Predicted Final Score: {prediction[0]:.2f}"
)