from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.db.session import database
from app.db.models.user import users as user_table
from app.utils.hashing import get_password_hash
from app.api.dependencies import get_current_user

print(f"Using get_current_user from: {get_current_user}")

router = APIRouter()

@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate):
    # Vérifiez si l'utilisateur existe
    query = user_table.select().where(user_table.c.email == user.email)
    existing_user = await database.fetch_one(query)

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
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
async def get_me(current_user=Depends(get_current_user)):
    print(f"Token reçu dans get_current_user : {token}")
    print("get_me endpoint called")
    print(f"get_current_user: {get_current_user}")
    return UserOut(**current_user)