from pydantic import BaseModel
from typing import Optional, Union
from datetime import date as DateType

class GamesBase(BaseModel):
    creator_id: int
    category_id: int
    name_game: str
    photo_game: Optional[str] = None
    description: Optional[str] = None
    link: Optional[str] = None
    date: Optional[DateType] = None
    file_id: Optional[str] = None
    state: Optional[str] = None

class GamesCreate(GamesBase):
    pass

class GamesResponse(GamesBase):
    game_id: int

    class Config:
        from_attributes = True

