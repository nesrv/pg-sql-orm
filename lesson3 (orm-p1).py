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

# https://pythonru.com/biblioteki/ustanovka-i-podklyuchenie-sqlalchemy-k-baze-dannyh


print("Запрос выполнен")
