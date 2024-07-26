import os
import time
from celery import Celery
from dotenv import load_dotenv

from src.services.upload_image import ImageUploader

load_dotenv(".env")

app = Celery(__name__)
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@app.task(name="create_task")
def create_task(b, c):
    time.sleep(1)
    return b + c

@app.task(name="upload_image")
def upload_image_task(filename, file_content):
    ImageUploader.write_file(filename, file_content)
    return {"message": "File written successfully"}