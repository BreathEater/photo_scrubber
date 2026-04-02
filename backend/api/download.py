from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/download/{session_id}")
async def download_zip(session_id: str):
   path = f"uploads/{session_id}/scrubbed.zip"
   if os.path.exists(path):
       return FileResponse(path, filename="scrubbed_photos.zip")
   return {"error": "File expired or not found"}


