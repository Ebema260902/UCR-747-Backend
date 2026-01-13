from sqlalchemy import Column, Integer, String
from app.database import Base

class Creator(Base):
    __tablename__ = "Creator"

    creator_id = Column(Integer, primary_key=True, index=True)
    name_creator = Column(String, nullable=False)
    photo_creator = Column(String)
    state = Column(String)
    career = Column(String)

