from sqlalchemy import Column, Integer, String

from app.db.database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)

    file_name = Column(String, nullable=False)

    blob_url = Column(String, nullable=False)