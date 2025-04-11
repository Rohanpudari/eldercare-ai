from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.health_monitor import check_health
from backend.agents.reminder_assistant import get_reminders
from backend.agents.social_companion import chat_with_elder

import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Eldercare AI Backend is running"}

@app.post("/monitor")
def monitor():
    return {"status": check_health()}

@app.post("/alert")
def alert(message: str = "Emergency Alert"):
    return {"alert": f"Alert received: {message}"}

@app.get("/reminders")
def reminders_endpoint():
    df = pd.read_csv('backend/data/daily_reminder.csv')
    return {"reminders": df['reminder'].tolist()}

@app.get("/safety-check")
def safety_check():
    df = pd.read_csv('backend/data/safety_monitoring.csv')
    latest = df.iloc[-1]
    event = latest.get("event", "No safety event recorded.")
    return {"safety_status": event}

@app.post("/chat")
def chat_endpoint(message: str):
    response = chat_with_elder(message)
    return {"response": response}
