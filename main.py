from src.predict import predict_sentiment

text = input("Enter your text: ")

prediction, confidence = predict_sentiment(text)

print("\nPrediction:", prediction)
print(f"Confidence: {confidence:.2f}")