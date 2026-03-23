from fastapi import APIRouter
from api.stats import router as stats_router

router = APIRouter()

api_router.include_router(stats_router, prefix="/stats", tags["stats"])

