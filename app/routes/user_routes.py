from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# "Base de datos" temporal
users_db = []

@router.get("/", response_model=list[User])
def get_users():
    return users_db


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    new_user = User(
        id=len(users_db) + 1,
        name=user.name,
        email=user.email
    )
    users_db.append(new_user)
    return new_user


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserCreate):
    for user in users_db:
        if user.id == user_id:
            user.name = user_data.name
            user.email = user_data.email
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}")
def delete_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
