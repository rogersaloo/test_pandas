import uvicorn
from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Sentiment(BaseModel):
    sentiment: str
    sentiment_probaility: float

nlp = pipeline("sentiment-analysis", 
               model="distilbert-base-uncased-finetuned-sst-2-english", 
               tokenizer="distilbert-base-uncased-finetuned-sst-2-english")

def generate(data):
    return nlp(data)


@app.get("/")
def root():
    return {"Welcome to dial Africa's API"}


@app.get('/api/v1/dialafrica')
def sentiment_anlysis(text: str):
    sentiment = generate(text)
    return sentiment[0]

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)