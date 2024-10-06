import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session


connection = psycopg2.connect(user="postgres", password="aatpotug")

engine = create_engine(
    "postgresql+psycopg2://postgres:aatpotug@localhost/train", echo=True)

engine.connect()


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


# добавление юзеров
# Base.metadata.create_all(bind=engine)

# with Session(autoflush=False, bind=engine) as db:
#     # tom = Person(name="Tom", age=38)
#     # db.add(tom)
#     # db.commit()    # print(tom.id)


#     alice = Person(name="Alice", age=33)
#     kate = Person(name="Kate", age=28)
#     db.add_all([alice, kate])
#     db.commit()


# чтение всех юзеров

# with Session(autoflush=False, bind=engine) as db:

#     people = db.query(Person).all()
#     for p in people:
#         print(f"{p.id}.{p.name} ({p.age})")

#     print("Объекты прочитаны")


# Получение данных
# with Session(autoflush=False, bind=engine) as db:
#     # чтение одного юзеров по id
#     first_person = db.get(Person, 1)
#     print(f"{first_person.name} - {first_person.age}")
    
#     people = db.query(Person).filter(Person.age > 30).all()
#     for p in people:
#         print(f"{p.id}.{p.name} ({p.age})")
        
#     first = db.query(Person).filter(Person.id==1).first()
#     print(f"{first.name} ({first.age})")    # Tom (38)

#     print("Объекты прочитаны")


# Обновление

with Session(autoflush=False, bind=engine) as db:
    # получаем один объект, у которого id=1
    tom = db.query(Person).filter(Person.id==1).first()
    if (tom != None):
        print(f"{tom.id}.{tom.name} ({tom.age})")   
        # 1.Tom (38)
 
        # изменениям значения
        tom.name = "Tomas"
        tom.age = 22
 
        db.commit() # сохраняем изменения
 
        # проверяем, что изменения применены в бд - получаем один объект, у которого имя - Tomas
        tomas = db.query(Person).filter(Person.id == 1).first()
        print(f"{tomas.id}.{tomas.name} ({tomas.age})")   
        
# Удаление
with Session(autoflush=False, bind=engine) as db:
    bob = db.query(Person).filter(Person.id==2).first()
    db.delete(bob)  # удаляем объект
    db.commit()     # сохраняем изменения