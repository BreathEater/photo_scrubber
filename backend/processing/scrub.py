import subprocess
import os
import shutil

def clean_photo_and_get_metadata(upload_file):

    os.makedirs("uploads", exist_ok=True)
    input_path = f"uploads/raw_{upload_file.filename}"
    output_path= f"uploads/clean_{upload_file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    original_size = os.path.getsize(input_path)

    # run exiftool:
    subprocess.run(["exiftool", "-all", "-o", output_path, input_path], check=True)

    #Calculate bytes_removed
    new_size = os.path.getsize(output_path)
    bytes_removed = max(0, original_size - new_size)

    os.remove(input_path)

    return output_path, bytes_removed


