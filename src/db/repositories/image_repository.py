from src.db.config.connection import DBConnectionHandler
from src.db.entities.images import Images
import os
import uuid

class ImageRepository:

    @classmethod
    def get_unique_filename_path(cls, filename):
        unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
        return unique_filename

    @classmethod
    def write_file(cls, unique_filename, filename):
        image_path = os.path.join('src', 'db', 'media', unique_filename)
        with open(image_path, 'wb') as f:
            f.write(filename)

    @classmethod
    def insert_image(cls, filename: str) -> None:
        unique_filename = cls.get_unique_filename_path(filename)
        cls.write_file(unique_filename, filename)

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
