from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    return ProjectService.create_project(db, project)

@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return ProjectService.get_projects(db)

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = ProjectService.get_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = ProjectService.delete_project(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted successfully"}