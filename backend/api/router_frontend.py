from fastapi import APIRouter
from api.get_index import router as index_router

frontend_router = APIRouter()

frontend_router.include_router(index_router)
