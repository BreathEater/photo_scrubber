import subprocess
import os

def clean_photo_and_get_metadata(input_path: str, output_path: str):

    original_size = os.path.getsize(input_path)

    # run exiftool:
    subprocess.run(["exiftool", "-all", "-o", output_path, input_path], check=True)

    #Calculate bytes_removed
    new_size = os.path.getsize(output_path)
    bytes_removed = max(0, original_size - new_size)

    return bytes_removed


