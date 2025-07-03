from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from src.models.schemas import TextRequest, PredictionResponse
from src.models.inference import TextClassifier
from src.config import APP_NAME, VERSION, API_SECRET_KEY

app = FastAPI(
    title=APP_NAME,
    description="API for text classifying using outperformed BOW-SVM model",
    version=VERSION
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the classifier
classifier = TextClassifier()

api_key_header = APIKeyHeader(name='X-API-Key')
async def verify_api_key(api_key: str=Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key


@app.get("/health", tags=['Healthy'], description="Endpoint to check if the API is up and running")
async def health_check(api_key: str=Depends(verify_api_key)):
    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "status": "up & running"
    }


@app.post("/predict", tags=['Classification'], 
        description='Analyzes the sentiment of provided texts', response_model=PredictionResponse)
async def predict(request: TextRequest, api_key: str=Depends(verify_api_key)):
    
    try:
        predictions = classifier.predict(request.texts)
        return PredictionResponse(predictions=predictions)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
