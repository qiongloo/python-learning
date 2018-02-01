##########
#偏函数
#通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))

def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
# 可以直接使用下面的代码创建一个新的函数
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))

#总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
#上面的函数
print(int2('1000000', base=10))
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：


kw = { 'base': 2 }
print(int('10010', **kw))

#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数

max2 = functools.partial(max,10)
#实际上是在左边加了10的参数
max2(5, 6, 7)
#等效为
args = (10, 5, 6, 7)
max(*args)





