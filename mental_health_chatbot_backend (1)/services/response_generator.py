
responses = {
    "sadness": "I'm sorry you're feeling sad. I'm here to listen.",
    "anxiety": "It sounds like you're anxious. Try taking a few deep breaths.",
    "stress": "Stress can be overwhelming. Try taking a short break.",
    "anger": "I understand you're feeling angry. Want to talk about it?",
    "loneliness": "You are not alone. I'm here with you.",
    "happiness": "That's wonderful to hear!"
}

def generate_response(emotion):
    return responses.get(emotion, "I'm here to listen. Tell me more.")
