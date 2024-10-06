# Создание подключения. Добавление записей
from sqlalchemy import create_engine



engine = create_engine(
    "postgresql+psycopg2://postgres:aatpotug@localhost/sqlalchemy_tuts",  echo=True, pool_size=6, max_overflow=10)
engine.connect()

print(engine)


cursor = engine.cursor()
sql_query = cursor.execute('table sqlalchemy_tuts')  


# https://pythonru.com/biblioteki/ustanovka-i-podklyuchenie-sqlalchemy-k-baze-dannyh
