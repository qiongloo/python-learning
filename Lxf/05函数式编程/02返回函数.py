#高级函数返回函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return  sum


f = lazy_sum(1,2,4,5,6,7)
print(f)
print(f())

#我们在函数lazy_sum中又定义了函数sum，并且，
#内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

#我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数


def count():
    fs = []
    for i in range(1, 4):
        def fff():
            return i*i
        fs.append(fff)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#练习

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
####注意点在于 变量的引用和存储
# def createCounter():
#     count =[0] #闭包外
#     def counter(): #闭包内
#         count[0] += 1
#         return count[0]
#     return counter
#

def createCounter():
    count = 0
    def counter(): #闭包内
        nonlocal count
        count = count + 1
        return count
    return counter

#nonlocal关键字用来在函数或其他作用域中修改外层(非全局)变量
#global关键字则是用于修改全局变量
#python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
