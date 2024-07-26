from pydantic import BaseModel

class Image(BaseModel):
    filename: str

class ImageUploadResponse(BaseModel):
    message: str
    filename: str
    task_id: str