from fastapi import FastAPI
from app.routes import auth, process

app = FastAPI()

# Include routes from other modules
app.include_router(auth.router)
app.include_router(process.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}

