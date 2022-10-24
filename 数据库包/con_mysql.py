import pymysql

host = "localhost"
user = "root"
password = "123456"
port = 3306
database = "novel"

con = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
cursor = con.cursor()
cursor.execute('select * from novel;')

result = cursor.fetchall()
print(result)
cursor.close()
con.close()
