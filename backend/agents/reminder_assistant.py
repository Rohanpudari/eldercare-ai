from backend.models.phi_model import ask_phi

def get_reminders():
    prompt = "List today's reminders for the elderly person."
    return ask_phi(prompt)
