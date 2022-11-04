from sqlalchemy.orm import Session

from core.database.models.users_model.users import Users
from core.database.schemas.users_schema.user_schema import UserBase


def create_user(session: Session, user: UserBase) -> Users:
    db_user = Users(
        email=user.email,
        password=user.password
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
