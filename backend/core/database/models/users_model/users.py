from sqlalchemy import Column, Integer, String, CHAR
from core.database.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50))
    password = Column(String(100))
