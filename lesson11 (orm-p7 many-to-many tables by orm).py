import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.orm import DeclarativeBase, Session

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



db_path = "postgresql+psycopg2://postgres:aatpotug@localhost/bookstore"

engine = create_engine(db_path, echo=True)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "books"

    id = Column(Integer, Identity(always=True), primary_key=True)
    title  = Column(String)



Base.metadata.create_all(bind=engine)
