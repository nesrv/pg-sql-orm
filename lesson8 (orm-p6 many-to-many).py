import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user="postgres", password="aatpotug")

engine = create_engine(
    "postgresql+psycopg2://postgres:aatpotug@localhost/train", echo=True)


connection = psycopg2.connect(user="postgres", password="aatpotug")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


cursor = connection.cursor()
sql_create_database = cursor.execute('create database bookstore')  

print("База данных создана")


cursor.close()
connection.close()


