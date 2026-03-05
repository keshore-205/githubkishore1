
from fastapi import FastAPI
from routes.chat import router as chat_router

app = FastAPI(title="Mental Health AI Chatbot API")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Mental Health Chatbot Backend Running"}
