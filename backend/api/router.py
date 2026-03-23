from fastapi import APIRouter
from api.scrub_post import router as scrub_router
from api.stats_get import router as stats_router

router = APIRouter()
router.include_router(stats_router, prefix="/stats")
router.include_router(scrub_router, prefix="/scrub")
