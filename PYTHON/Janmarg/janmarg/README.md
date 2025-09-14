# JANMARG - Content Moderation & Provenance System

## Overview
JANMARG is an end-to-end content moderation and provenance system designed for the Smart India Hackathon. The project aims to provide various services including text spam classification, image synthetic detection, image provenance checking, and image category classification through a unified FastAPI backend and a simple React frontend.

## Features
1. **Text Spam Classifier**: An API that classifies text as "spam" or "not spam".
2. **Image Synthetic Detector**: An API that determines if an image is AI-generated or real, providing confidence scores and artifact notes.
3. **Image Provenance Checker**: 
   - Extracts EXIF metadata from images.
   - Performs reverse image searches using TinEye, Google, or Bing.
   - Heuristic analysis to determine if an image is likely downloaded or reused.
4. **Image Category Classifier**: Classifies images into predefined categories such as news-photo, document, meme, ad, screenshot, portrait, and scene.

## Project Structure
```
janmarg
├── backend
│   ├── api
│   ├── train
│   ├── datasets
│   ├── tests
│   ├── evaluation
│   ├── demo
│   ├── requirements.txt
│   ├── .env.template
│   └── README.md
├── frontend
│   ├── src
│   ├── package.json
│   └── README.md
├── docker
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
├── .github
│   └── workflows
│       └── ci.yml
├── LICENSE
└── README.md
```

## Setup Instructions
### Backend
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd janmarg/backend
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Copy `.env.template` to `.env` and fill in the required values.

5. **Download datasets**:
   Run the dataset preparation scripts:
   ```
   python datasets/download_sms.py
   python datasets/download_images.py
   python datasets/prepare.py
   ```

6. **Train models**:
   ```
   python train/train_spam.py
   python train/train_synthetic.py
   python train/train_category.py
   ```

7. **Run the FastAPI application**:
   ```
   uvicorn api.main:app --reload
   ```

### Frontend
1. **Navigate to the frontend directory**:
   ```
   cd janmarg/frontend
   ```

2. **Install npm dependencies**:
   ```
   npm install
   ```

3. **Run the React application**:
   ```
   npm start
   ```

## Running with Docker
1. **Build and run the application**:
   ```
   cd docker
   docker-compose up --build
   ```

## Testing
Run unit tests for each module:
```
cd backend/tests
pytest
```

## Evaluation
To evaluate the models, run the evaluation scripts:
```
cd backend/evaluation
python eval_spam.py
python eval_synthetic.py
python eval_provenance.py
python eval_category.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Hugging Face Transformers for text models.
- PyTorch for deep learning frameworks.
- FastAPI for building the backend API.
- React for the frontend application.