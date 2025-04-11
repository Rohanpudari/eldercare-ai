import pandas as pd
from backend.models.phi_model import ask_phi

def check_health():
    # Load health vitals from CSV
    df = pd.read_csv('backend/data/health_monitoring.csv')

    # Check if expected columns exist
    if 'heart_rate' not in df.columns or 'blood_pressure' not in df.columns:
        return {"status": "Invalid CSV format. Expected 'heart_rate' and 'blood_pressure' columns."}

    # Get the latest row
    latest = df.iloc[-1]
    heart_rate = latest['heart_rate']
    blood_pressure = latest['blood_pressure']

    # Compose prompt
    prompt = (
        f"You are a virtual eldercare assistant.\n"
        f"Today's latest health vitals are:\n"
        f"- Heart Rate: {heart_rate}\n"
        f"- Blood Pressure: {blood_pressure}\n"
        f"Do these values raise any concern for an elderly person?"
    )

    return ask_phi(prompt)
