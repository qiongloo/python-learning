#使用sqllite数据库

#SQLite是一种嵌入式数据库，它的数据库就是一个文件。


import sqlite3

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
#
# #cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user(id, name) values(\'1\',\'mach\')')
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()



###查询记录

# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# ###执行查询结果集
# cursor.execute('select *  from user where id = ?',('1',))
# #通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()




#####练习


import os, sqlite3
#print(os.path.dirname(__file__))

db_file = os.path.join(os.path.dirname(__file__),'test2.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    if not (isinstance(low,int) and isinstance(high,int)):
        return '区间数字必须整型！'
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select name from user where score >=? and score <=? order by score ',(low,high))
    data = cursor.fetchall()
    #print(data)
    list1 = []
    for a in data:
        list1.append(a[0])
    cursor.close()
    conn.close()
    return list1



# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')


print(sqlite3.version)
print(sqlite3.version_info)












