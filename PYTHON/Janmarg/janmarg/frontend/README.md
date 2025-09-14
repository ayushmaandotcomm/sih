# Frontend README.md

# JANMARG Frontend

This README provides instructions for setting up and running the frontend of the JANMARG project, which is an end-to-end content moderation and provenance system.

## Prerequisites

- Node.js (version 14 or higher)
- npm (Node Package Manager)

## Installation

1. Navigate to the frontend directory:

   ```bash
   cd janmarg/frontend
   ```

2. Install the required npm packages:

   ```bash
   npm install
   ```

## Running the Frontend

To start the frontend application, run the following command:

```bash
npm start
```

This will start the development server and open the application in your default web browser. The frontend will be available at `http://localhost:3000`.

## API Endpoints

The frontend interacts with the following backend API endpoints:

1. **Spam Classifier**
   - Endpoint: `/api/spam`
   - Method: POST
   - Request Body: `{ "text": "string" }`
   - Response: `{ "result": "spam/not spam", "confidence": number }`

2. **Synthetic Image Detector**
   - Endpoint: `/api/synthetic`
   - Method: POST
   - Request Body: `{ "image": "base64 string" }`
   - Response: `{ "result": "AI-generated/real", "confidence": number, "artifact_note": "string" }`

3. **Image Provenance Checker**
   - Endpoint: `/api/provenance`
   - Method: POST
   - Request Body: `{ "image": "base64 string" }`
   - Response: `{ "exif_data": "object", "matches": [{ "url": "string", "date": "string" }] }`

4. **Image Category Classifier**
   - Endpoint: `/api/category`
   - Method: POST
   - Request Body: `{ "image": "base64 string" }`
   - Response: `{ "category": "string", "confidence": number }`

## Building for Production

To build the frontend for production, run:

```bash
npm run build
```

This will create an optimized build of the application in the `build` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.

## Acknowledgments

- This project utilizes various libraries and frameworks, including React and FastAPI, to provide a seamless user experience and robust backend services.