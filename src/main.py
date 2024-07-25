from fastapi import FastAPI, File, UploadFile
from src.schemas import ImageUploadResponse

app = FastAPI()

@app.get("/health-check")
async def add_nums(a: int, b: int):
    return {"result": a + b}

@app.post("/upload/image/", response_model=ImageUploadResponse)
async def upload_image(image: UploadFile = File(...)):
    return {"message": "Image file received successfully", "filename": image.filename}