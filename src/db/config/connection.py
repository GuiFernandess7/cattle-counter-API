from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DBConnectionHandler:

    def __init__(self) -> None:
        db_user = os.getenv('POSTGRES_USER', 'root')
        db_password = os.getenv('POSTGRES_PASSWORD', 'myPassword')
        db_name = os.getenv('POSTGRES_DB', 'cattleCounter')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '5432')

        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'postgresql+psycopg2',
            db_user,
            db_password,
            db_host,
            db_port,
            db_name
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
