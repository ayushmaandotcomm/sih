import os
from PIL import Image
from PIL.ExifTags import TAGS
import requests

class ProvenanceChecker:
    def __init__(self):
        self.reverse_image_search_api = os.getenv("REVERSE_IMAGE_SEARCH_API")
        self.api_key = os.getenv("API_KEY")

    def extract_exif(self, image_path):
        """Extract EXIF data from an image."""
        image = Image.open(image_path)
        exif_data = {}
        if hasattr(image, '_getexif'):
            exif = image._getexif()
            if exif is not None:
                for tag_id, value in exif.items():
                    tag = TAGS.get(tag_id, tag_id)
                    exif_data[tag] = value
        return exif_data

    def reverse_image_search(self, image_path):
        """Perform a reverse image search using an external API."""
        with open(image_path, 'rb') as image_file:
            response = requests.post(
                self.reverse_image_search_api,
                files={'file': image_file},
                headers={'Authorization': f'Bearer {self.api_key}'}
            )
            return response.json()

    def check_provenance(self, image_path):
        """Check the provenance of an image."""
        exif_data = self.extract_exif(image_path)
        search_results = self.reverse_image_search(image_path)

        provenance_info = {
            "exif_data": exif_data,
            "search_results": search_results
        }
        return provenance_info