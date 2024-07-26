#from google.cloud import storage
#from src.db.config.base import BUCKET_NAME
import uuid
import os

from errors.write_file_error import WriteImageError

class ImageUploader:

    @classmethod
    def __get_unique_filename_path(cls, filename):
        """Temp method"""
        unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
        return unique_filename

    @classmethod
    def write_file(cls, filename, file_content):
        """Temp method"""
        unique_filename = cls.__get_unique_filename_path(filename)
        image_path = os.path.join('media', unique_filename)

        try:
            with open(image_path, 'wb') as f:
                f.write(file_content)
        except Exception as e:
            raise WriteImageError(f"Error writing image to folder: {e}")

    """ @classmethod
    def send_to_bucket(cls, file_path, unique_filename):
        ""Not implemented""
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(unique_filename)

        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to {cls.GCS_BUCKET_NAME} as {unique_filename}") """