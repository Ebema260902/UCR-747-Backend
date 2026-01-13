from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.routes.categories import router as categories_router
from app.routes.creators import router as creators_router
from app.routes.projects import router as projects_router
from app.routes.academic_materials import router as academic_materials_router
from app.routes.games import router as games_router
from app.models.project import Project
from app.models.games import Games
from app.models.academic_material import AcademicMaterial
from app.models.creator import Creator
from app.models.category import Category

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories_router)
app.include_router(creators_router)
app.include_router(projects_router)
app.include_router(academic_materials_router)
app.include_router(games_router)

@app.get("/")
def root():
    return {"message": "Backend funcionando 🚀"}

@app.get("/dashboard")
def get_dashboard(db: Session = Depends(get_db)):
    """Returns total counts of projects, games, academic materials, creators, and categories."""
    projects_count = db.query(func.count(Project.project_id)).scalar() or 0
    games_count = db.query(func.count(Games.game_id)).scalar() or 0
    materials_count = db.query(func.count(AcademicMaterial.material_id)).scalar() or 0
    creators_count = db.query(func.count(Creator.creator_id)).scalar() or 0
    categories_count = db.query(func.count(Category.category_id)).scalar() or 0
    
    return {
        "projects": projects_count,
        "games": games_count,
        "materials": materials_count,
        "creators": creators_count,
        "categories": categories_count
    }
