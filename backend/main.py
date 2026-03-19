from fastapi import FastAPI, UploadFile, File
   from fastapi.responses import FileResponse
   import shutil
   import os
   import subprocess

   app = FastAPI()
   UPLOAD_DIR = "uploads"
   os.makedirs(UPLOAD_DIR, exist_ok=True)

   # Mock stats for now
   PHOTOS_CLEANED = 0

   @app.get("/api/stats")
   async def get_stats():
       return {"photos_cleaned": PHOTOS_CLEANED}

   @app.post("/api/scrub")
   async def scrub_image(file: UploadFile = File(...)):
       global PHOTOS_CLEANED

       # 1. Save the original file to /uploads
       input_path = os.path.join(UPLOAD_DIR, f"orig_{file.filename}")
       output_path = os.path.join(UPLOAD_DIR, f"scrubbed_{file.filename}")

       with open(input_path, "wb") as buffer:
           shutil.copyfileobj(file.file, buffer)

       # 2. Use Exiftool (which you have in your Dockerfile!) to scrub
       # -all= removes all metadata
       subprocess.run(["exiftool", "-all=", "-o", output_path, input_path])

       PHOTOS_CLEANED += 1

       # 3. Return the clean file to the browser
       return FileResponse(output_path, media_type="image/jpeg", filename=f"scrubbed_{file.filename}")


