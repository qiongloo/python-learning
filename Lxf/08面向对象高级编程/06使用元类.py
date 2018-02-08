###元类

class Hello(object):
    def hello(self, name='world'):
        print('hello, %s' % name)


h = Hello()
h.hello()
print(type(Hello))
print(type(h))



def fn(self, name='world'): # 先定义函数
     print('Hello, %s.' % name)
#使用type生成类



Hello = type('Hello', (object,), dict(hello=fn))
# 要创建一个class对象，type()函数依次传入3个参数：
#
#     class的名称；
#     继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#     class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
#

s = type('Goll',(object,),dict(hello = fn))
print(type(s)) #<class 'type'>

s2 = s()
print(type(s2)) #<class '__main__.Goll'>

s2.hello('ddd')

# metaclass
#
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
#
#

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# __new__()方法接收到的参数依次是：
#     当前准备创建的类的对象；
#     类的名字；
#     类继承的父类集合；
#     类的方法集合。

#有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
print(L)

print([1,2,3]+[2,3])



####总体而言就是增加属性 或者方法
#案例2
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
import logging
try:
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
except Exception as e:
    logging.exception(e)

# 保存到数据库：
#u.save()






