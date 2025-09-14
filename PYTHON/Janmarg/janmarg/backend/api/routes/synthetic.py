from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import cv2
import numpy as np
from models.synthetic_detector import SyntheticDetector  # Assuming this is the model class

router = APIRouter()

class SyntheticResponse(BaseModel):
    is_synthetic: bool
    confidence: float
    artifact_note: str

# Initialize the synthetic detector model
synthetic_detector = SyntheticDetector()

@router.post("/detect_synthetic", response_model=SyntheticResponse)
async def detect_synthetic(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Process the image with the synthetic detector
    is_synthetic, confidence, artifact_note = synthetic_detector.predict(img)

    return SyntheticResponse(
        is_synthetic=is_synthetic,
        confidence=confidence,
        artifact_note=artifact_note
    )