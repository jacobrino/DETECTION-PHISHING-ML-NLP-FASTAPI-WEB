# app/schema.py

from pydantic import BaseModel

class EmailRequest(BaseModel):
    subject: str
    body: str

class PredictionResponse(BaseModel):
    prediction: str
    proba: float | None = None
