# Создание подключения. Добавление записей
import psycopg2
from sqlalchemy import create_engine

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="aatpotug")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


cursor = connection.cursor()
sql_create_database = cursor.execute(
    'create database sqlalchemy_tuts')  # Создаем базу данных


cursor.close()
connection.close()

print("Запрос выполнен")


# https://pythonru.com/biblioteki/ustanovka-i-podklyuchenie-sqlalchemy-k-baze-dannyh


engine = create_engine(
    "postgresql+psycopg2://postgres:1111@aatpotug/sqlalchemy_tuts",  echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)
engine.connect()

print(engine)
