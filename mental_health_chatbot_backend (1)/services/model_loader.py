
import joblib

model = joblib.load("model/emotion_classifier_model.pkl")

def predict_emotion(text):
    prediction = model.predict([text])[0]
    return prediction
