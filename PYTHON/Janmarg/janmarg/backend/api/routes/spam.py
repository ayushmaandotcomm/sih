from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.spam_classifier import SpamClassifier

router = APIRouter()
spam_classifier = SpamClassifier()

class SpamRequest(BaseModel):
    text: str

class SpamResponse(BaseModel):
    is_spam: bool
    confidence: float

@router.post("/spam", response_model=SpamResponse)
async def classify_spam(request: SpamRequest):
    try:
        is_spam, confidence = spam_classifier.predict(request.text)
        return SpamResponse(is_spam=is_spam, confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))