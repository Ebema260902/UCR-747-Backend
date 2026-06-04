from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db, engine, Base
from app.routes.categories import router as categories_router
from app.routes.creators import router as creators_router
from app.routes.projects import router as projects_router
from app.routes.academic_materials import router as academic_materials_router
from app.routes.games import router as games_router
from app.routes.admin import router as admin_router
from app.models.project import Project
from app.models.games import Games
from app.models.academic_material import AcademicMaterial
from app.models.creator import Creator
from app.models.category import Category


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Al iniciar: crear tablas y poblar con datos si la BD está vacía
    Base.metadata.create_all(bind=engine)
    try:
        from scripts.seed_data import seed_data
        seed_data()
    except Exception as e:
        print(f"Advertencia al hacer seed: {e}")
    yield
    # (aquí iría cleanup al apagar, si fuera necesario)


app = FastAPI(lifespan=lifespan)

# CORS: permite localhost en desarrollo y cualquier origen en producción (Vercel, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(categories_router)
app.include_router(creators_router)
app.include_router(projects_router)
app.include_router(academic_materials_router)
app.include_router(games_router)
app.include_router(admin_router)

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
