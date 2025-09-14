from fastapi import APIRouter, HTTPException
from typing import List, Dict
from ..models.provenance_checker import ProvenanceChecker
import os

router = APIRouter()
provenance_checker = ProvenanceChecker()

@router.post("/provenance/check", response_model=Dict[str, List[str]])
async def check_provenance(image_url: str):
    try:
        # Extract EXIF data
        exif_data = provenance_checker.extract_exif(image_url)
        
        # Perform reverse image search
        search_results = provenance_checker.reverse_image_search(image_url)
        
        return {
            "exif": exif_data,
            "search_results": search_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))