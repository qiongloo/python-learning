###########
# 装饰器

#函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2018-02-01')
    return ''
f = now
print(f())

#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
print(f.__name__)


#我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorato

def log(f):
    def wrapper(*args, **kw):
        print('call %s()' % f.__name__)
        return f(*args, **kw)
    return wrapper
#借助Python的@语法，把decorator置于函数的定义处：
#@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print('12-12')
print(now())
# call now()
# 12-12

#传入参数的修饰器
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

print(now())
# execute now():
# 2015-3-25

#和两层嵌套的decorator相比，3层嵌套的效果是这样的： now = log('execute')(now)
print(now.__name__) #wrapper
#返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#Python内置的functools.wraps就是干这个事的

#完整的decorator
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
print(now())
print(now.__name__) #now


###带参数
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


#定义wrapper()的前面加上@functools.wraps(func)即可。

# 练习
#
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **key):
        t1 = time.time() * 1000
        s =  fn(*args, **key)
        t2 = time.time() * 1000
        print('%s executed in %s ms' % (fn.__name__,t2-t1))
        return s
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')



#再思考一下能否写出一个@log的decorator，使它既支持：
def log(text=None):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not text:
                print('函数', func.__name__, '被调用了')
            else:
                print('函数', func.__name__, '被调用了，额外信息是:', text)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@log
def f():
    print('酱油')
f()
@log()
def f():
    print('酱油')
f()

def f():
    print('生抽')
log()(f)()

@log('大家好我是额外')
def f():
    print('老抽')












