from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from processing.scrub import clean_photo_and_get_metadata
from api.db.db_trigger import trigger_db_procedure

router = APIRouter()

@router.post("/scrub")
async def scrub_post(file: UploadFile = File(...)):

    output_path, bytes_removed = clean_photo_and_get_metadata(file)

    trigger_db_procedure("stats_record", bytes_removed)
    
    return FileResponse(output_path)

