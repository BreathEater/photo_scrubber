from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from processing.scrub import clean_photos_and_get_metadata
from api.db.db_trigger import trigger_db_procedure

router = APIRouter()

@router.post("/scrub")
async def scrub_post(files: list[UploadFile] = File(...)):

    zip_buffer, bytes_removed = clean_photos_and_get_metadata(files)

    trigger_db_procedure("stats_record", len(files), bytes_removed)
    
    return StreamingResponse(
        zip_buffer,
        media_type="application/x-zip-compressed",
        headers={"Content-Disposition": f"attachment; filename=scrubbed_{len(files)}_photos.zip"}
            )

