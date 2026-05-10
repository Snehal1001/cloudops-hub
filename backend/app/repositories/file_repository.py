from sqlalchemy.orm import Session

from app.models.file import File

class FileRepository:

    @staticmethod
    def create(
        db: Session,
        file_name: str,
        blob_url: str
    ):
        file = File(
            file_name=file_name,
            blob_url=blob_url
        )

        db.add(file)

        db.commit()

        db.refresh(file)

        return file