from fastapi import APIRouter

router = APIRouter()

@router.post("/process-text")
def process_text(text: str):
    # Simple example: reversing the input text
    return {"processed_text": text[::-1]}
