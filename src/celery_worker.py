import os
import time
from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

app = Celery(__name__)
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@app.task(name="upload_image")
def upload_image_task(filename, file_content):
    from services.upload_image import ImageUploader
    ImageUploader.write_file(filename, file_content)
    return "File uploaded successfully"