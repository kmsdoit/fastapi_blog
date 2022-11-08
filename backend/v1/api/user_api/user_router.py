from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database.base import get_db
from core.database.schemas.users_schema.user_schema import UserBase, User
from core.database.models.users_model.users import Users
from v1.api.user_api.crud import create_user, user_exist_email_func
from core.auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/sign-up", response_model=User)
async def sign_up(user_info: UserBase, session: Session = Depends(get_db)):
    return create_user(session, user_info)


@router.post("/login")
async def login(user_info: UserBase, session: Session = Depends(get_db)):
    return user_exist_email_func(session, user_info)


@router.post("/me", dependencies=[Depends(JWTBearer())])
async def me(user_info: UserBase):
    return user_info
