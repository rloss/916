from fastapi import FastAPI
from app.routers import items, scoring

app = FastAPI(title="Enneagram Test API")

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(scoring.router, prefix="/score", tags=["score"])

@app.get("/")
def root():
    return {"message": "Enneagram Test API is running"}
