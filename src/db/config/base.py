from sqlalchemy.orm import declarative_base
import os

Base = declarative_base()
IMAGE_BASE_PATH = os.environ.get('IMAGE_BASE_PATH')
