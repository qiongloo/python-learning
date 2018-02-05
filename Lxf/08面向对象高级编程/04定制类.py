####定制类

#本小节告诉我们内置函数的覆盖和自定义覆盖
#__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

class Student(object):
    __slots__ = ('name','age')

    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Student object(name: %s) ' % self.name

    __repr__ = __str__

#定义好__str__()方法，返回一个好看的字符串
#__repr__()是为调试服务的
#但是通常__str__()和__repr__()代码都是一样的



# 如果一个类想被用于for ... in循环，
# 类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise  StopIteration()
        return  self.a


for n in Fib():
    print(n)


#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[100])

#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a, b = b, a+b
            return  L

f = Fib()
print(f[0:5])



#Python还有另一个机制，那就是写一个__getattr__()方法，
# 动态返回一个属性

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        elif attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.score)

print(s.age())


#一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Mech')
print(s())


#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# class Student(object):
#     def __call__(self):
#         print('My name is %s.' % self.name)

class Student(object):
    pass

print(callable(Student()))
print(callable(max))

print(callable([1,3,4]))
print(callable('str'))




#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


