from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.storage_service import load_submissions

from routes.form_routes import router as form_router
from routes.clustering_routes import router as clustering_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(form_router)
app.include_router(clustering_router)

@app.get("/", response_model=list)
async def root():
    """
    Return all saved form submissions as JSON.
    """
    return load_submissions()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
