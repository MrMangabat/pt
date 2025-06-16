from fastapi import APIRouter
from services.clustering_service import trigger_clustering
from services.storage_service import load_submissions

router = APIRouter()

@router.post("/trigger-clustering")
async def trigger_clustering_route():
    """
    Run clustering on existing submissions and return cluster labels.
    """
    clusters = trigger_clustering()
    return {"clusters": clusters}

@router.get("/export-data")
async def export_data():
    """
    Export all raw submission data.
    """
    return load_submissions()
