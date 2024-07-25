from sqlalchemy.orm import declarative_base
from google.cloud import storage
import os

Base = declarative_base()

# GCP
BUCKET_NAME = os.environ.get('BUCKET_NAME')

client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)
