from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Games(Base):
    __tablename__ = "Games"

    game_id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("Creator.creator_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("Category.category_id"), nullable=False)
    name_game = Column(String, nullable=False)
    photo_game = Column(String)
    description = Column(String)
    link = Column(String)
    date = Column(Date)
    file_id = Column(String)
    state = Column(String)

