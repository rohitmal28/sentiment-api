from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: List[str]

def detect_sentiment(sentence: str):
    s = sentence.lower()

    happy_words = ["love","great","good","happy","awesome","excellent","amazing"]
    sad_words = ["hate","bad","terrible","sad","awful","worst","horrible"]

    if any(w in s for w in happy_words):
        return "happy"

    if any(w in s for w in sad_words):
        return "sad"

    return "neutral"

@app.post("/sentiment")
def sentiment(data: SentimentRequest):

    results = []

    for sentence in data.sentences:
        results.append({
            "sentence": sentence,
            "sentiment": detect_sentiment(sentence)
        })

    return {"results": results}