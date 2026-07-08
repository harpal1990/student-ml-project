import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load data
from utils import load_config

config = load_config()

data = pd.read_csv(
    "../" + config["paths"]["dataset"]
)

# Features
X = data[
    [
        "study_hours",
        "sleep_hours",
        "attendance",
        "previous_marks"
    ]
]

# Target
y = data["final_score"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=config["training"]["test_size"],
    random_state=config["training"]["random_state"]
)

# Train
model = LinearRegression()

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(
    y_test,
    predictions
)

print(f"Mean Absolute Error: {mae}")

# Show learned weights
print("\nFeature Weights")

for feature, weight in zip(X.columns, model.coef_):
    print(f"{feature}: {weight}")

print(f"\nIntercept: {model.intercept_}")

# Save model
joblib.dump(
    model,
    "../" + config["paths"]["model"]
)

print("\nModel saved as student_model.pkl")