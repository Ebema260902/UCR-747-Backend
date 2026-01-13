from pydantic import BaseModel
from typing import Optional

class CreatorBase(BaseModel):
    name_creator: str
    photo_creator: Optional[str] = None
    state: Optional[str] = None
    career: Optional[str] = None

class CreatorCreate(CreatorBase):
    pass

class CreatorResponse(CreatorBase):
    creator_id: int

    class Config:
        from_attributes = True

