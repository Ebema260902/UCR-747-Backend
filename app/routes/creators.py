from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text, func
from app.database import get_db
from app.models.creator import Creator
from app.models.project import Project
from app.models.games import Games
from app.models.academic_material import AcademicMaterial
from app.schemas.creator import CreatorCreate, CreatorResponse

router = APIRouter(
    prefix="/creators",
    tags=["Creators"]
)

@router.post("/", response_model=CreatorResponse)
def create_creator(creator: CreatorCreate, db: Session = Depends(get_db)):
    new_creator = Creator(**creator.model_dump())
    db.add(new_creator)
    db.commit()
    db.refresh(new_creator)
    return new_creator


@router.get("/", response_model=list[CreatorResponse])
def get_creators(db: Session = Depends(get_db)):
    return db.query(Creator).all()


@router.get("/{creator_id}", response_model=CreatorResponse)
def get_creator(creator_id: int, db: Session = Depends(get_db)):
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator no encontrado")
    return creator


@router.get("/{creator_id}/summary")
def get_creator_summary(creator_id: int, db: Session = Depends(get_db)):
    """Returns creator info plus counts of related projects, games, and materials."""
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator no encontrado")
    
    projects_count = db.query(func.count(Project.project_id)).filter(
        Project.creator_id == creator_id
    ).scalar() or 0
    
    games_count = db.query(func.count(Games.game_id)).filter(
        Games.creator_id == creator_id
    ).scalar() or 0
    
    materials_count = db.query(func.count(AcademicMaterial.material_id)).filter(
        AcademicMaterial.creator_id == creator_id
    ).scalar() or 0
    
    return {
        "creator_id": creator.creator_id,
        "name_creator": creator.name_creator,
        "photo_creator": creator.photo_creator,
        "state": creator.state,
        "career": creator.career,
        "projects_count": projects_count,
        "games_count": games_count,
        "materials_count": materials_count
    }


@router.put("/{creator_id}", response_model=CreatorResponse)
def update_creator(creator_id: int, creator: CreatorCreate, db: Session = Depends(get_db)):
    db_creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not db_creator:
        raise HTTPException(status_code=404, detail="Creator no encontrado")
    
    for key, value in creator.model_dump().items():
        setattr(db_creator, key, value)
    
    db.commit()
    db.refresh(db_creator)
    return db_creator


@router.delete("/{creator_id}")
def delete_creator(creator_id: int, db: Session = Depends(get_db)):
    creator = db.query(Creator).filter(Creator.creator_id == creator_id).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator no encontrado")

    db.delete(creator)
    db.commit()
    return {"message": "Creator eliminado"}

