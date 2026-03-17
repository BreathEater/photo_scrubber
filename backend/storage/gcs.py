 from google.cloud import storage
   from .base import StorageProvider

   class GCSStorage(StorageProvider):
       def __init__(self, bucket_name):
           self.client = storage.Client()
           self.bucket = self.client.bucket(bucket_name)

       def save_photo(self, photo_bytes, filename):
           blob = self.bucket.blob(filename)
           blob.upload_from_string(photo_bytes)
           return blob.public_url


