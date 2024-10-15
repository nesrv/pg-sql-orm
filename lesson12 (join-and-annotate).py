import psycopg2

conn = psycopg2.connect(dbname="train", user="postgres",
                        password="aatpotug", host="127.0.0.1", port="5432")

cursor = conn.cursor()
 

conn.autocommit = True
# sql1 = "create table t3(id integer, txt text)"
sql2 = "select * from table_t1"
sql3 = '''
SELECT * FROM table_t1 t1, table_t2 t2 
-- WHERE t1.id = t2.id
''' # декартово произведение

sql4 = '''
SELECT * FROM table_t1 t1
INNER JOIN table_t2 t2 ON t1.id = t2.id
'''

sql5 = '''
SELECT * FROM table_t1 t1
LEFT JOIN table_t2 t2 ON t1.id = t2.id
'''

sql6 = '''
SELECT * FROM table_t1 t1
RIGHT JOIN table_t2 t2 ON t1.id = t2.id
'''

sql7 = '''
SELECT * FROM table_t1 t1
FULL JOIN table_t2 t2 ON t1.id = t2.id
'''

sql8 = '''
SELECT * FROM table_t1 t1
CROSS JOIN table_t2 t2
'''

sql9 = '''
SELECT * FROM table_t1 t1
NATURAL JOIN table_t2 t2
'''
 
# выполняем код sql
cursor.execute(sql9)
print(*cursor.fetchall(), sep='')
print("Запрос выполнен")
 
cursor.close()
conn.close()