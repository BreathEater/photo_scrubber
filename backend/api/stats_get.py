from fastapi import APIRouter
from processing.stats import get_photos_cleaned_count

router = APIRouter()

@router.get("/stats")
async def get_stats():
    count = get_photos_cleaned_count()
    return {"photos_cleaned": count}

