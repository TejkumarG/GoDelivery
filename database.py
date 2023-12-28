from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, session

SQLALCHEMY_DATABASE_URL = "sqlite:///temp.db"


Base = declarative_base()


def get_db() -> session:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=0)
    Base.metadata.create_all(bind=engine)  # Create tables
    local_session = sessionmaker(bind=engine)
    db = local_session()
    try:
        yield db
    finally:
        db.close()
