
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, nullable =False)
    title  = Column(String)
   