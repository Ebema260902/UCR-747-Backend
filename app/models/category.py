from sqlalchemy import Column, Integer, String
from app.database import Base

class Category(Base):
    __tablename__ = "Category"

    category_id = Column(Integer, primary_key=True, index=True)
    name_category = Column(String, nullable=False)
