from fastapi import FastAPI, File, UploadFile
from src.schemas import ImageUploadResponse

app = FastAPI()

@app.post("/upload/image/", response_model=ImageUploadResponse)
async def upload_image(image: UploadFile = File(...)):
    return {"message": "Image file received successfully", "filename": image.filename}