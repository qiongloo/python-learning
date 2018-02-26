###使用SQLAlchemy


#在Python中，最有名的ORM框架是SQLAlchemy。

listdata = [('1','Michael'),('2','Bob'),('3','Adam')]
print(listdata)



class User(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name


list2 = [User('1','Michael'),User('2','Bob'),User('3','Adam')]
print(list2)


# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

#定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user2'

    # 表的结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://test:@120.27.49.**:3306/Test')
DBSession = sessionmaker(bind=engine)




#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_user = User(id='6', name='Bob')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()



# 可见，关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。
# 如何从数据库表中查询数据呢？有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供的查询接口如下：

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='1').one()
print('type:',type(user))
print('name:',user.name)

session.close()





#
# class User(Base):
#     __tablename__ = 'user'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')
#
# class Book(Base):
#     __tablename__ = 'book'
#
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))

#
#
#
#
#
#
#
#
#
#
#
#

#

























