import os
import joblib

from preprocess import clean_text

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model and vectorizer
model_path = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")

vectorizer_path = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_sentiment(text):

    # Clean input
    cleaned_text = clean_text(text)

    # Vectorize
    vectorized_text = vectorizer.transform([cleaned_text])

    # Prediction
    prediction = model.predict(vectorized_text)[0]

    # Confidence score
    probability = model.predict_proba(vectorized_text).max()

    return prediction, probability