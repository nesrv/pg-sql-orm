import psycopg2

conn = psycopg2.connect(dbname="train", user="postgres",
                        password="aatpotug", host="127.0.0.1", port="5432")

cursor = conn.cursor()
 

conn.autocommit = True
# sql1 = "create table t3(id integer, txt text)"
sql2 = "select * from table_t1"
 
# выполняем код sql
cursor.execute(sql2)
print(*cursor.fetchall(), sep='\n')
print("Запрос выполнен")
 
cursor.close()
conn.close()