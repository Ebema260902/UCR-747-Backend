from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.categories import router as categories_router
from app.routes.creators import router as creators_router
from app.routes.projects import router as projects_router
from app.routes.academic_materials import router as academic_materials_router
from app.routes.games import router as games_router

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
