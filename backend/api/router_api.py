from fastapi import APIRouter
from api.post_scrub import router as scrub_router
from api.get_stats import router as stats_router
from api.get_log import router as log_router       # Add this
from api.download import router as download_router # Add this

api_router = APIRouter()
api_router.include_router(stats_router)
api_router.include_router(scrub_router)
api_router.include_router(log_router)       # Register it
api_router.include_router(download_router)  # Register it


