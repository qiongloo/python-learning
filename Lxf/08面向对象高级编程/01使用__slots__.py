


class Student(object):
    pass


s =  Student()
s.name = 'Michael'



#为实例绑定方法

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)


#为了给所有实例都绑定方法，可以给class绑定方法：
Student.set_age = set_age

#上面的set_age方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

class Stu(object):
    __slots__ = ('name','age')

s = Stu()
s.name = 'haode'
s.age = 'age'
#s.sore = 0  是会报错的


#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

class Stu1(Stu):
    pass

g = Stu1()
g.score = 888

class Stu2(Stu):
    __slots__ = ('age2')
g = Stu2()
g.name = 'd3'
#g.score = 888 报错