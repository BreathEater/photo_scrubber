from fastapi import APIRouter
from api.db.db_trigger import trigger_db_function

router = APIRouter()

@router.get("/stats")
async def get_stats():
    result = trigger_db_function("stats_read") or (0, 0)
    return{
            "photos_cleaned": result[0] or 0,
            "bytes_removed": result[1] or 0
        }

