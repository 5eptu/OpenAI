from fastapi import APIRouter, Header, HTTPException

router = APIRouter()

API_KEY = "your_api_key"

@router.get("/secure-data")
def get_secure_data(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"secure_data": "This is protected content!"}
