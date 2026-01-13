from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProjectBase(BaseModel):
    creator_id: int
    category_id: int
    name_project: str
    description: Optional[str] = None
    photo_project: Optional[str] = None
    date: Optional[date] = None
    file_id: Optional[str] = None
    state: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    project_id: int

    class Config:
        from_attributes = True

