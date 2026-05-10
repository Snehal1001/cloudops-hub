from pydantic import BaseModel

class FileResponse(BaseModel):
    id: int
    file_name: str
    blob_url: str

    class Config:
        from_attributes = True