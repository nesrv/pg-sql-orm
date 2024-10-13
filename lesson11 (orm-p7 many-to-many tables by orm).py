import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Identity, Text
from sqlalchemy.orm import DeclarativeBase, Session

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



db_path = "postgresql+psycopg2://postgres:aatpotug@localhost/bookstore"

engine = create_engine(db_path, echo=True)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "books"

    id = Column(Integer, Identity(always=True), primary_key=True)
    title  = Column(Text, nullable=False)


class AuthorShip(Base):
    __tablename__ = "authorship"
    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, primary_key=True)
    seq_num = Column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)
