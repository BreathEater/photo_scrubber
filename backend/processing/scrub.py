import subprocess
import os
import shutil
import zipfile
import io
import uuid

def clean_photos_and_get_metadata(upload_files):
   session_id = str(uuid.uuid4())
   raw_dir, clean_dir = f"uploads/{session_id}/raw", f"uploads/{session_id}/clean"
   os.makedirs(raw_dir, exist_ok=True); os.makedirs(clean_dir, exist_ok=True)

   for f in upload_files:
       with open(os.path.join(raw_dir, f.filename), "wb") as b: shutil.copyfileobj(f.file, b)

   # ONE exiftool call for the entire directory
   subprocess.run(["exiftool", "-all=", "-tagsFromFile", "@", "-Orientation", "-o", f"{clean_dir}/", f"{raw_dir}/"], check=True)

   zip_buffer = io.BytesIO()
   bytes_removed = 0
   with zipfile.ZipFile(zip_buffer, "w") as zf:
       for f_name in os.listdir(clean_dir):
           c_p, r_p = os.path.join(clean_dir, f_name), os.path.join(raw_dir, f_name)
           bytes_removed += max(0, os.path.getsize(r_p) - os.path.getsize(c_p))
           zf.write(c_p, arcname=f_name)

   shutil.rmtree(f"uploads/{session_id}")
   zip_buffer.seek(0)
   return zip_buffer, bytes_removed


