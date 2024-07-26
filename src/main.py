from fastapi import FastAPI, File, UploadFile, Body
from fastapi.responses import JSONResponse
from src.schemas import ImageUploadResponse
from src.celery_worker import create_task, upload_image_task
from celery.result import AsyncResult

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
    file_content = await image.read()
    task = upload_image_task.delay(image.filename, file_content)
    return ImageUploadResponse(message="Process started", filename=image.filename, task_id=task.id)

@app.get("/result/image/{task_id}")
async def get_result(task_id: str):
    task_result = AsyncResult(task_id)

    if task_result.state == 'PENDING':
        return {"status": "pending"}
    elif task_result.state == 'SUCCESS':
        return {"status": "completed", "result": task_result.result}
    elif task_result.state == 'FAILURE':
        return {"status": "failed", "error": str(task_result.info)}
    else:
        return {"status": task_result.state}