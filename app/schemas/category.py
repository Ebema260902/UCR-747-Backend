from pydantic import BaseModel

class CategoryBase(BaseModel):
    name_category: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    category_id: int

    class Config:
        from_attributes = True
