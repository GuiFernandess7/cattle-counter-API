from src.db.config.connection import DBConnectionHandler
from src.db.entities.images import Images

class ImageRepository:

    @classmethod
    def insert_image(cls, filename: str, count = None) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = Images(
                    filename=filename,
                    count=count
                )
                database.session.add(new_registry)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception