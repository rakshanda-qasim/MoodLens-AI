import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_sentiment

# Page configuration
st.set_page_config(
    page_title="MoodLens AI",
    page_icon="🧠",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
        }

        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #4A90E2;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
            color: #666666;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🧠 MoodLens AI</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI-Powered Sentiment Analysis</div>',
    unsafe_allow_html=True
)

# Text input
user_input = st.text_area(
    "Enter your text below:",
    height=180,
    placeholder="Type a movie review, tweet, or comment..."
)

# Analyze button
if st.button("Analyze Sentiment"):

    if user_input.strip() != "":

        prediction, confidence = predict_sentiment(user_input)

        st.markdown("---")
        st.subheader("Prediction Result")

        # Positive
        if prediction == "positive":

            st.success("😊 Positive Sentiment Detected")

        # Negative
        else:

            st.error("😠 Negative Sentiment Detected")

        # Confidence
        st.write(f"### Confidence Score: {confidence:.2f}")

        st.progress(float(confidence))

    else:

        st.warning("⚠ Please enter some text.")