# README for JANMARG Backend

## Overview
JANMARG is an end-to-end content moderation and provenance system designed for the Smart India Hackathon. This backend service provides APIs for various functionalities including text spam classification, image synthetic detection, image provenance checking, and image category classification.

## Project Structure
The backend is organized into several directories:
- **api**: Contains the FastAPI application and route definitions.
- **train**: Contains training scripts and configuration files for the models.
- **datasets**: Scripts for downloading and preparing datasets.
- **tests**: Unit tests for each module.
- **evaluation**: Scripts for evaluating model performance.
- **demo**: A script to run a demo of the application.

## Setup Instructions

### Prerequisites
- Python 3.10+
- pip
- Docker (for containerized deployment)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd janmarg/backend
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy the `.env.template` to `.env` and fill in the required values.

### Running the Application
To run the FastAPI application locally:
```
uvicorn api.main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

### Docker Deployment
To run the application using Docker:
1. Build the Docker image:
   ```
   docker build -f docker/Dockerfile.backend -t janmarg-backend .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:8000 --env-file .env janmarg-backend
   ```

3. Access the application at `http://127.0.0.1:8000`.

## API Endpoints
- **Spam Classifier**: `/api/spam` - Classifies text as spam or not spam.
- **Synthetic Detector**: `/api/synthetic` - Detects if an image is AI-generated or real.
- **Provenance Checker**: `/api/provenance` - Checks image provenance and extracts EXIF data.
- **Category Classifier**: `/api/category` - Classifies images into predefined categories.

## Running Tests
To run the unit tests:
```
pytest tests/
```

## Evaluation
To evaluate the models, run the respective evaluation scripts located in the `evaluation` directory.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
This project utilizes various open-source libraries and datasets. Please refer to the respective documentation for usage and licensing details.