# File: /janmarg/janmarg/backend/demo/run_demo.py

import requests

def run_demo():
    # Example text for spam classification
    text_example = "Congratulations! You've won a $1000 Walmart gift card. Click here to claim your prize."
    
    # Call the spam classification API
    spam_response = requests.post("http://localhost:8000/spam", json={"text": text_example})
    print("Spam Classification Response:", spam_response.json())

    # Example image for synthetic detection
    image_example_path = "path/to/your/image.jpg"
    with open(image_example_path, "rb") as image_file:
        synthetic_response = requests.post("http://localhost:8000/synthetic", files={"image": image_file})
        print("Synthetic Detection Response:", synthetic_response.json())

    # Example image for provenance checking
    provenance_image_path = "path/to/your/provenance_image.jpg"
    with open(provenance_image_path, "rb") as provenance_file:
        provenance_response = requests.post("http://localhost:8000/provenance", files={"image": provenance_file})
        print("Provenance Checking Response:", provenance_response.json())

    # Example image for category classification
    category_image_path = "path/to/your/category_image.jpg"
    with open(category_image_path, "rb") as category_file:
        category_response = requests.post("http://localhost:8000/category", files={"image": category_file})
        print("Category Classification Response:", category_response.json())

if __name__ == "__main__":
    run_demo()