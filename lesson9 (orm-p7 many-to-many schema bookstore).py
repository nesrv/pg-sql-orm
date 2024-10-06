import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



# engine = create_engine(
#     "postgresql+psycopg2://postgres:aatpotug@localhost/bookstore", echo=True)


connection = psycopg2.connect(dbname="bookstore",user="postgres", password="aatpotug")
# conn = psycopg2.connect(dbname="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


cursor = connection.cursor()

# sql_create_database = cursor.execute('CREATE SCHEMA bookstore;')  
sql_create_database = cursor.execute('ALTER DATABASE bookstore SET search_path = bookstore, public;')  
  

print("ALTER DATABASE bookstore SET search_path = bookstore, public;")

# Создаем базу данных

cursor.close()
connection.close()
