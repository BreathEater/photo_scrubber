from fastapi import APIRouter, UploadFile, File
from processing.scrub import clean_photos
from api.db.db_trigger import trigger_db_procedure

router = APIRouter()

@router.post("/scrub")
async def scrub_post(files: list[UploadFile] = File(...)):
   # 1. Process files
   session_id, bytes_removed, log_text = clean_photos(files)

   # 2. Update Database Stats
   trigger_db_procedure("stats_record", len(files), bytes_removed)

   # 3. Return JSON (Body, not Header, to avoid Nginx size limits)
   return {
       "session_id": session_id,
       "log": log_text
   }


