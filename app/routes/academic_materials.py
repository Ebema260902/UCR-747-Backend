from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.models.academic_material import AcademicMaterial
from app.schemas.academic_material import AcademicMaterialCreate, AcademicMaterialResponse

router = APIRouter(
    prefix="/academic-materials",
    tags=["Academic Materials"]
)

@router.post("/", response_model=AcademicMaterialResponse)
def create_academic_material(material: AcademicMaterialCreate, db: Session = Depends(get_db)):
    new_material = AcademicMaterial(**material.model_dump())
    db.add(new_material)
    db.commit()
    db.refresh(new_material)
    return new_material


@router.get("/", response_model=list[AcademicMaterialResponse])
def get_academic_materials(
    state: Optional[str] = Query(None, description="Filter by state"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    creator_id: Optional[int] = Query(None, description="Filter by creator ID"),
    db: Session = Depends(get_db)
):
    query = db.query(AcademicMaterial)
    
    if state is not None:
        query = query.filter(AcademicMaterial.state == state)
    if category_id is not None:
        query = query.filter(AcademicMaterial.category_id == category_id)
    if creator_id is not None:
        query = query.filter(AcademicMaterial.creator_id == creator_id)
    
    return query.all()


@router.get("/search", response_model=list[AcademicMaterialResponse])
def search_materials(
    q: str = Query(..., description="Search query"),
    db: Session = Depends(get_db)
):
    """Search academic materials by name and description using LIKE."""
    query = db.query(AcademicMaterial).filter(
        (AcademicMaterial.name_material.like(f"%{q}%")) |
        (AcademicMaterial.description.like(f"%{q}%"))
    )
    return query.all()


@router.get("/{material_id}", response_model=AcademicMaterialResponse)
def get_academic_material(material_id: int, db: Session = Depends(get_db)):
    material = db.query(AcademicMaterial).filter(AcademicMaterial.material_id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Academic Material no encontrado")
    return material


@router.put("/{material_id}", response_model=AcademicMaterialResponse)
def update_academic_material(material_id: int, material: AcademicMaterialCreate, db: Session = Depends(get_db)):
    db_material = db.query(AcademicMaterial).filter(AcademicMaterial.material_id == material_id).first()
    if not db_material:
        raise HTTPException(status_code=404, detail="Academic Material no encontrado")
    
    for key, value in material.model_dump().items():
        setattr(db_material, key, value)
    
    db.commit()
    db.refresh(db_material)
    return db_material


@router.delete("/{material_id}")
def delete_academic_material(material_id: int, db: Session = Depends(get_db)):
    material = db.query(AcademicMaterial).filter(AcademicMaterial.material_id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Academic Material no encontrado")

    db.delete(material)
    db.commit()
    return {"message": "Academic Material eliminado"}

