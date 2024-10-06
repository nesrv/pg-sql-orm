import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase



connection = psycopg2.connect(user="postgres", password="aatpotug")

engine = create_engine("postgresql+psycopg2://postgres:aatpotug@localhost/train")

engine.connect()

class Base(DeclarativeBase): pass
  
class Person(Base):
    __tablename__ = "people"
  
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)
 
print("База данных и таблица созданы")