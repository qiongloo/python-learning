##使用mysql
#$ pip install mysql-connector-python --allow-external mysql-connector-python


import mysql.connector



# 导入MySQL驱动
import mysql.connector
# 连接数据库
#本地数据库
#conn = mysql.connector.connect(user="test", password="test456852", database="test")
#远程数据库连接
conn = mysql.connector.connect(host='120.**.**.**', user='test', passwd='', db='Test', port=3306)
cursor = conn.cursor()

# 创建user表:
#cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user2 (id, name) values (%s, %s)', ['2', 'Michael'])
# cursor.rowcount

# 提交事务:
# conn.commit()
# cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user2 where id =%s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()










