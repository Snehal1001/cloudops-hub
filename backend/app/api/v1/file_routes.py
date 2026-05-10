from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.blob_service import BlobService
from app.repositories.file_repository import FileRepository
from app.schemas.file import FileResponse

router = APIRouter(
    prefix="/api/v1/files",
    tags=["Files"]
)

@router.post(
    "/upload",
    response_model=FileResponse
)
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    blob_url = BlobService.upload_file(
        file.filename,
        file.file
    )

    saved_file = FileRepository.create(
        db=db,
        file_name=file.filename,
        blob_url=blob_url
    )

    return saved_file