from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = FastAPI()

# Load your fine-tuned model (update path if needed)
tokenizer = AutoTokenizer.from_pretrained("./fine-tuned-distilbert-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("./fine-tuned-distilbert-sentiment")

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    review = data.get("review", "")
    inputs = tokenizer(review, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    outputs = model(**inputs)
    pred = torch.argmax(outputs.logits, dim=1).item()
    return {"prediction": "positive" if pred == 1 else "negative"}
