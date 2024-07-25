from fastapi import FastAPI, File, UploadFile, Body
from fastapi.responses import JSONResponse
from src.schemas import ImageUploadResponse
from src.celery_worker import create_task

app = FastAPI()

@app.post("/health-check")
async def add_nums(data=Body(...)):
    """Test celery"""
    x = data["x"]
    y = data["y"]
    task = create_task.delay(x, y)
    return JSONResponse({"Result": task.get()})

@app.post("/upload/image/", response_model=ImageUploadResponse)
async def upload_image(image: UploadFile = File(...)):
    return {"message": "Image file received successfully", "filename": image.filename}