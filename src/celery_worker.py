import os
from celery import Celery
from dotenv import load_dotenv

from db.repositories.image_repository import ImageRepository

load_dotenv(".env")

app = Celery(__name__)
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@app.task(name="upload_image")
def upload_image_task(filename, file_content):
    from services.upload_image import ImageUploader
    results = ImageUploader.get_results_from_image(filename=filename, file_content=file_content, min_contour_area=30)
    #ImageRepository.insert_image(filename=filename, count=results)
    return {"message": "Image processed", "data": results}