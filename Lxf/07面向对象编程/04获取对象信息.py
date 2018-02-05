#判断对象类型，使用type()函数
print(type(123))
print(type('str'))
print(type(None))
print(type(abs)) #<class 'builtin_function_or_method'>

class Animal(object):
    pass

a = Animal()
print(type(a)) #<class '__main__.Animal'>

import types

def fn():
     pass


print(type(fn) == types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)

print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))


#要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('ABC'))

#在len()函数内部，它自动去调用该对象的__len__()方法
print(len('ABC'))

class MyDog(object):
     def __len__(self):
         return 100;

dog = MyDog()
print(len(dog))



#把属性和方法列出来是不够的，
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x

obj = MyObject()
fn = getattr(obj,'power')
print(fn())  #81  调用fn()与调用obj.power()是一样的


#在我们不知道对象信息的时候 才使用上面的方法


