from fastapi import APIRouter, HTTPException, status
from models.form_models import FormSubmission
from services.storage_service import save_submission

router = APIRouter()

@router.post("/submit-form-data", status_code=status.HTTP_201_CREATED)
async def submit_form(payload: FormSubmission):
    try:
        save_submission(payload.model_dump())
        return {"message": "Form data saved"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e),)
