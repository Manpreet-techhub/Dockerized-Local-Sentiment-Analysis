from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from transformers import pipeline
import os
import torch
import uvicorn
from dotenv import load_dotenv


app = FastAPI()

API_KEY = os.getenv('API_KEY')
sentiment_pipeline = pipeline("sentiment-analysis")

class TextIn(BaseModel):
    text: str

load_dotenv()

@app.post("/analyze")
async def analyze_text(text_in: TextIn, request: Request):
    if request.headers.get("Authorization") != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    result = sentiment_pipeline(text_in.text)
    output = result[0]
    sentiment = output["label"]
    score = output["score"]
    return {
        "sentiment": sentiment,
        "score": score
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



