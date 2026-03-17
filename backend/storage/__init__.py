 import os

   def get_storage():
       storage_type = os.getenv("STORAGE_TYPE", "LOCAL").upper()

       if storage_type == "GCS":
           from .gcs import GCSStorage
           return GCSStorage(bucket_name=os.getenv("GCS_BUCKET_NAME"))
       else:
           from .local import LocalStorage
           return LocalStorage(upload_dir=os.getenv("LOCAL_UPLOAD_DIR", "./uploads"))


