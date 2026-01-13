from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base

class Project(Base):
    __tablename__ = "Project"

    project_id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("Creator.creator_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("Category.category_id"), nullable=False)
    name_project = Column(String, nullable=False)
    description = Column(String)
    photo_project = Column(String)
    date = Column(Date)
    file_id = Column(String)
    state = Column(String)

