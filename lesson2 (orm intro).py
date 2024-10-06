# Создание подключения. Добавление записей

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import psycopg2

# pg_database = "postgresql://postgres:aatpotug@localhost/train"

engine = create_engine("postgresql+psycopg2://postgres:aatpotug@localhost/train")

engine.connect()

print(engine)


# engine = create_engine(pg_database)


# class Base(DeclarativeBase):
#     pass


# class TableT(Base):
#     __tablename__ = "public.t3"

    # id = Column(Integer)
    # txt = Column(String)


# Base.metadata.create_all(bind=engine)


# with Session(autoflush=False, bind=engine) as db:
#     # создаем объект  для добавления в бд
#     row_2 = TableT(id=2, txt='два')
#     db.add(row_2)     # добавляем в бд
#     db.commit()     # сохраняем изменения
#     print(row_2.id)   # можно получить установленный id


print("Запрос выполнен")
