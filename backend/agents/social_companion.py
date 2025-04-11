from backend.models.phi_model import ask_phi

def chat_with_elder(message: str):
    prompt = f"As a friendly companion for an elderly person, respond to: '{message}'"
    return ask_phi(prompt)
