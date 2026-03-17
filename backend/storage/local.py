 import os
   from .base import StorageProvider

   class LocalStorage(StorageProvider):
       def __init__(self, upload_dir):
           self.upload_dir = upload_dir
           os.makedirs(upload_dir, exist_ok=True)

       def save_photo(self, photo_bytes, filename):
           path = os.path.join(self.upload_dir, filename)
           with open(path, "wb") as f:
               f.write(photo_bytes)
           return path

       def get_photo(self, filename):
           path = os.path.join(self.upload_dir, filename)
           if not os.path.exists(path):
               return None
           with open(path, "rb") as f:
               return f.read()


