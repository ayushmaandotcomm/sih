from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import spam, synthetic, provenance, category

app = FastAPI()

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes for each service
app.include_router(spam.router, prefix="/spam", tags=["Spam Classifier"])
app.include_router(synthetic.router, prefix="/synthetic", tags=["Synthetic Detector"])
app.include_router(provenance.router, prefix="/provenance", tags=["Provenance Checker"])
app.include_router(category.router, prefix="/category", tags=["Category Classifier"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the JANMARG API!"}