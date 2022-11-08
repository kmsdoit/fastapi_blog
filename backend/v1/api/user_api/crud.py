from typing import Dict

from fastapi import HTTPException
import bcrypt
import jwt
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from core.database.models.users_model.users import Users
from core.database.schemas.users_schema.user_schema import UserBase
from dotenv import load_dotenv
from core.auth.auth_handler import signJWT
from os import environ

load_dotenv()

def create_user(session: Session, user: UserBase) -> Users:
    db_user = Users(
        email=user.email,
        password=user.password,
    )

    user_email_exist = (
        session.query(Users)
        .filter(Users.email == db_user.email)
        .first()
    )

    if user_email_exist:
        raise HTTPException(status_code=400, detail="email already registerd")
    user_password_encode = user.password.encode("utf-8")
    hash_pw = (bcrypt.hashpw(user_password_encode, bcrypt.gensalt()))
    hash_pw = hash_pw.decode("utf-8")
    db_user.password = hash_pw

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def user_exist_email_func(session: Session, user: UserBase) -> dict:
    db_user = Users(
        email=user.email,
        password=user.password
    )

    user_exist_email = session.query(Users).filter(Users.email == db_user.email).first()

    if len(user_exist_email.email) < 0:
        raise HTTPException(status_code=404, detail="user not found")

    user_password = user.password.encode("utf-8")
    hashed_password = user_exist_email.password.encode("utf-8")

    is_verified = bcrypt.checkpw(user_password, hashed_password)

    if not is_verified:
        raise HTTPException(status_code=403, detail="you are password is not correct")

    result = {
        "result": "ok",
        "data": user_exist_email,
        "jwt_token" : signJWT(str(user_exist_email.id))
    }

    return result
