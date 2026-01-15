from pydantic import BaseModel
from typing import Optional, Union
from datetime import date as DateType

class AcademicMaterialBase(BaseModel):
    creator_id: int
    category_id: int
    name_material: str
    description: Optional[str] = None
    photo_material: Optional[str] = None
    date: Optional[DateType] = None
    file_id: Optional[str] = None
    state: Optional[str] = None

class AcademicMaterialCreate(AcademicMaterialBase):
    pass

class AcademicMaterialResponse(AcademicMaterialBase):
    material_id: int

    class Config:
        from_attributes = True

