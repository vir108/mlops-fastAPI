from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

sentiment_model = pipeline("sentiment-analysis")

class PredictionRequest(BaseModel):
  query_string: str

app = FastAPI()

@app.get("/health")
def health():
    return "Service is Online."

@app.post("/performSentimentAnalysis")
def perform_sentiment_analysis(request: PredictionRequest):
    # Run sentiment analysis
    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence) 
    print(f"Sentiment test: {sentiment_query_sentence} === {sentiment}")
    return sentiment
