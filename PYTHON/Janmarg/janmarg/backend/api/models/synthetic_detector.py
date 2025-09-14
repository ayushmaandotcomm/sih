from fastapi import APIRouter
from pydantic import BaseModel
import torch
from torchvision import transforms
from PIL import Image
import io

router = APIRouter()

class SyntheticDetectionRequest(BaseModel):
    image: bytes

class SyntheticDetectionResponse(BaseModel):
    is_synthetic: bool
    confidence: float
    artifact_note: str

class SyntheticDetector:
    def __init__(self, model_path: str):
        self.model = torch.load(model_path)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    def predict(self, image_bytes: bytes) -> SyntheticDetectionResponse:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            output = self.model(image)
            is_synthetic = output.argmax(dim=1).item() == 1  # Assuming 1 is synthetic
            confidence = torch.softmax(output, dim=1).max().item()
            artifact_note = "Possible artifacts detected." if is_synthetic else "No artifacts detected."
        return SyntheticDetectionResponse(is_synthetic=is_synthetic, confidence=confidence, artifact_note=artifact_note)

detector = SyntheticDetector(model_path="path/to/synthetic_model.pth")

@router.post("/detect_synthetic", response_model=SyntheticDetectionResponse)
async def detect_synthetic(request: SyntheticDetectionRequest):
    return detector.predict(request.image)