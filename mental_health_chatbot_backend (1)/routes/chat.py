
from fastapi import APIRouter
from pydantic import BaseModel
from services.model_loader import predict_emotion
from services.response_generator import generate_response
from utils.preprocess import clean_text

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    cleaned = clean_text(request.message)
    emotion = predict_emotion(cleaned)
    response = generate_response(emotion)

    return {
        "user_message": request.message,
        "emotion": emotion,
        "response": response
    }
