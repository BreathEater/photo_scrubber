 from abc import ABC, abstractmethod

   class StorageProvider(ABC):
       @abstractmethod
       def save_photo(self, photo_bytes, filename):
           pass

       @abstractmethod
       def get_photo(self, filename):
           pass


