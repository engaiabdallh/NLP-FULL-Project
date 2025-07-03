# src/models/schemas.py
from pydantic import BaseModel, Field
from typing import List

class TextRequest(BaseModel):
    texts: List[str] = Field(..., min_length=1, description="List of input texts to classify")

    class Config:
        json_schema_extra = {
            "example": {
                "texts": [
                    "This is a great product!",
                    "I hate this service",
                    "The product works as expected"
                ]
            }
        }

class SentimentPrediction(BaseModel):
    text: str
    sentiment: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "This is a great product!",
                "sentiment": "Positive"
            }
        }

class PredictionResponse(BaseModel):
    predictions: List[SentimentPrediction]

    class Config:
        json_schema_extra = {
            "example": {
                "predictions": [
                    {
                        "text": "This is a great product!",
                        "sentiment": "Positive"
                    },
                    {
                        "text": "I hate this service",
                        "sentiment": "Negative"
                    }
                ]
            }
        }