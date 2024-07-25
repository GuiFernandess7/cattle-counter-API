from src.db.config.connection import DBConnectionHandler
from google.cloud import storage
from src.db.entities.images import Images
from src.db.config.base import BUCKET_NAME
import os
import uuid

class ImageRepository:

    @classmethod
    def get_unique_filename_path(cls, filename):
        unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
        return unique_filename

    @classmethod
    def write_file(cls, unique_filename, file_content):
        image_path = os.path.join('src', 'db', 'media', unique_filename)
        with open(image_path, 'wb') as f:
            f.write(file_content)

    @classmethod
    def __upload_image_to_bucket(cls, file_path, unique_filename):
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(unique_filename)

        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to {cls.GCS_BUCKET_NAME} as {unique_filename}")

    @classmethod
    def insert_image(cls, filename: str, file_content: bytes) -> None:
        unique_filename = cls.get_unique_filename_path(filename)
        local_file_path = os.path.join('src', 'db', 'media', unique_filename)

        cls.write_file(unique_filename, file_content)
        #cls.__upload_image_to_bucket(local_file_path, unique_filename)

        with DBConnectionHandler() as database:
            try:
                new_registry = Images(
                    filename=unique_filename
                )
                database.session.add(new_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception