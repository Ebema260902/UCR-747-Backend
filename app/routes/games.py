from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.games import Games
from app.schemas.games import GamesCreate, GamesResponse

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)

@router.post("/", response_model=GamesResponse)
def create_game(game: GamesCreate, db: Session = Depends(get_db)):
    new_game = Games(**game.model_dump())
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game


@router.get("/", response_model=list[GamesResponse])
def get_games(db: Session = Depends(get_db)):
    return db.query(Games).all()


@router.get("/{game_id}", response_model=GamesResponse)
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Games).filter(Games.game_id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game no encontrado")
    return game


@router.put("/{game_id}", response_model=GamesResponse)
def update_game(game_id: int, game: GamesCreate, db: Session = Depends(get_db)):
    db_game = db.query(Games).filter(Games.game_id == game_id).first()
    if not db_game:
        raise HTTPException(status_code=404, detail="Game no encontrado")
    
    for key, value in game.model_dump().items():
        setattr(db_game, key, value)
    
    db.commit()
    db.refresh(db_game)
    return db_game


@router.delete("/{game_id}")
def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Games).filter(Games.game_id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game no encontrado")

    db.delete(game)
    db.commit()
    return {"message": "Game eliminado"}

