## Создание подключения через psycopg2 
## Добавление таблиц и записей


import psycopg2

conn = psycopg2.connect(dbname="train", user="postgres",
                        password="aatpotug", host="127.0.0.1", port="5432")

cursor = conn.cursor()
 

conn.autocommit = True
# sql1 = "create table t3(id integer, txt text)"
sql2 = "insert into t3(id, txt) values (1,'раз')"
 
# выполняем код sql
cursor.execute(sql2)
print("Запрос выполнен")
 
cursor.close()
conn.close()


# \! chcp 1251