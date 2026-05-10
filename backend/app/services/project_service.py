from sqlalchemy.orm import Session
from app.repositories.project_repository import ProjectRepository
from app.schemas.project import ProjectCreate

class ProjectService:

    @staticmethod
    def create_project(db: Session, project_data: ProjectCreate):
        return ProjectRepository.create(db, project_data)

    @staticmethod
    def get_projects(db: Session):
        return ProjectRepository.get_all(db)

    @staticmethod
    def get_project(db: Session, project_id: int):
        return ProjectRepository.get_by_id(db, project_id)

    @staticmethod
    def delete_project(db: Session, project_id: int):
        return ProjectRepository.delete(db, project_id)