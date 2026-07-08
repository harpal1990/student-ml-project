import pandas as pd
import joblib

from utils import load_config

config = load_config()

model = joblib.load(
    "../" + config["paths"]["model"]
)

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