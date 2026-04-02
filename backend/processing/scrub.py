import subprocess
import os
import shutil
import zipfile
import io
import uuid

def clean_photos(upload_files):
   session_id = str(uuid.uuid4())
   session_dir = f"uploads/{session_id}"
   raw_dir, clean_dir = f"{session_dir}/raw", f"{session_dir}/clean"
   os.makedirs(raw_dir, exist_ok=True)
   os.makedirs(clean_dir, exist_ok=True)

   # 1. Save raw files to disk
   for f in upload_files:
       with open(os.path.join(raw_dir, f.filename), "wb") as b:
           shutil.copyfileobj(f.file, b)

   # 2. Capture the Log BEFORE scrubbing (using the forgiving decoder)
   process = subprocess.run(["exiftool", "-S", raw_dir], capture_output=True)
   log_text = process.stdout.decode('utf-8', errors='replace')

   # 3. Run the one-shot batch scrub
   subprocess.run(["exiftool", "-all=", "-tagsFromFile", "@", "-Orientation", "-o", f"{clean_dir}/", f"{raw_dir}/"], check=True)

   # 4. Create the ZIP on disk for later download
   zip_path = f"{session_dir}/scrubbed.zip"
   bytes_removed = 0
   with zipfile.ZipFile(zip_path, "w") as zf:
       for f_name in os.listdir(clean_dir):
           c_p, r_p = os.path.join(clean_dir, f_name), os.path.join(raw_dir, f_name)
           bytes_removed += max(0, os.path.getsize(r_p) - os.path.getsize(c_p))
           zf.write(c_p, arcname=f_name)

   # Note: We do NOT delete the session_dir yet so the user can download the ZIP
   return session_id, bytes_removed, log_text


