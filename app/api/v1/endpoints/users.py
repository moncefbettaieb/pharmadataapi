from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserOut
from app.db.session import database
from app.db.models.user import users as user_table
from app.utils.hashing import get_password_hash
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate):
    query = user_table.insert().values(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        subscription_level="free",
        quota=100,
        usage=0
    )
    user_id = await database.execute(query)
    return { "id": user_id, "email": user.email }

@router.get("/me", response_model=UserOut)
async def get_me(current_user = Depends(get_current_user)):
    # current_user est probablement un dict retourné par la DB
    # On le convertit en modèle Pydantic avant de le renvoyer
    return UserOut(**current_user)