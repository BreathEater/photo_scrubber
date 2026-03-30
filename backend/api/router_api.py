from fastapi import APIRouter
from api.post_scrub import router as scrub_router
from api.get_stats import router as stats_router

api_router = APIRouter()
api_router.include_router(stats_router)
api_router.include_router(scrub_router)
