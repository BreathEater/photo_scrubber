from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="/frontend/templates")

@router.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse(request, "index.html")
