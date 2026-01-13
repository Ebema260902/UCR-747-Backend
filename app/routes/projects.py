from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import Optional
from app.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectResponse

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(**project.model_dump())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@router.get("/", response_model=list[ProjectResponse])
def get_projects(
    state: Optional[str] = Query(None, description="Filter by state"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    creator_id: Optional[int] = Query(None, description="Filter by creator ID"),
    db: Session = Depends(get_db)
):
    query = db.query(Project)
    
    if state is not None:
        query = query.filter(Project.state == state)
    if category_id is not None:
        query = query.filter(Project.category_id == category_id)
    if creator_id is not None:
        query = query.filter(Project.creator_id == creator_id)
    
    return query.all()


@router.get("/search", response_model=list[ProjectResponse])
def search_projects(
    q: str = Query(..., description="Search query"),
    db: Session = Depends(get_db)
):
    """Search projects by name and description using LIKE."""
    query = db.query(Project).filter(
        (Project.name_project.like(f"%{q}%")) |
        (Project.description.like(f"%{q}%"))
    )
    return query.all()


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project no encontrado")
    return project


@router.get("/{project_id}/full")
def get_project_full(project_id: int, db: Session = Depends(get_db)):
    """Returns a project with creator and category names using JOINs."""
    result = db.execute(
        text("""
            SELECT 
                p.project_id,
                p.creator_id,
                p.category_id,
                p.name_project,
                p.description,
                p.photo_project,
                p.date,
                p.file_id,
                p.state,
                c.name_creator,
                cat.name_category
            FROM Project p
            LEFT JOIN Creator c ON p.creator_id = c.creator_id
            LEFT JOIN Category cat ON p.category_id = cat.category_id
            WHERE p.project_id = :project_id
        """),
        {"project_id": project_id}
    ).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="Project no encontrado")
    
    return {
        "project_id": result[0],
        "creator_id": result[1],
        "category_id": result[2],
        "name_project": result[3],
        "description": result[4],
        "photo_project": result[5],
        "date": str(result[6]) if result[6] else None,
        "file_id": result[7],
        "state": result[8],
        "creator_name": result[9],
        "category_name": result[10]
    }


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = db.query(Project).filter(Project.project_id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project no encontrado")
    
    for key, value in project.model_dump().items():
        setattr(db_project, key, value)
    
    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project no encontrado")

    db.delete(project)
    db.commit()
    return {"message": "Project eliminado"}

