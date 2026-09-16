import joblib
import pandas as pd
from pathlib import Path


# Load model
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "random_forest_smote.pkl"
FEATURE_PATH = Path(__file__).resolve().parent.parent / "models" / "feature_names.pkl"

model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURE_PATH)


def predict_transaction(transaction):
    """
    Predict whether a transaction is fraudulent.

    transaction should be a dictionary containing
    the same features used during training.
    """

    df = pd.DataFrame([transaction])

    # Make sure feature order matches training
    df = df[feature_names]

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        result = "FRAUD"
    else:
        result = "NORMAL"

    return {
        "prediction": result,
        "fraud_probability": round(float(probability), 4)
    }


if __name__ == "__main__":
    print("Fraud detection model loaded successfully.")
    print(f"Number of features: {len(feature_names)}")