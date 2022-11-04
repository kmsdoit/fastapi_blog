from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv

load_dotenv()

host = environ["HOST"]
user = environ["DB_USER"]
password = environ["DB_PASSWORD"]
database = environ["DATABASE"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
