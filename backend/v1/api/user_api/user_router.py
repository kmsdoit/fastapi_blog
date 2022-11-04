from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database.base import get_db
from core.database.schemas.users_schema.user_schema import UserBase, User
from core.database.models.users_model.users import Users
from v1.api.user_api.crud import create_user
router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/sign-up", response_model=User)
async def sign_up(user_info: UserBase, session: Session = Depends(get_db)):
    db_user = (
        session.query(Users)
        .filter(Users.email == user_info.email)
        .first()
    )

    if db_user:
        raise HTTPException(status_code=400, detail="email already registerd")

    return create_user(session, user_info)
