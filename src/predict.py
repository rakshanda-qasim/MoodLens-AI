import joblib
from src.preprocess import clean_text

# Load model and vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict_sentiment(text):
    cleaned = clean_text(text)

    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]

    probability = model.predict_proba(vectorized).max()

    return prediction, probability