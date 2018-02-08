#函数
#内置函数 绝对值abs(100)  最大值max(2, 3, 1, -5)

#数据类型转换
int('123')
#123
int(12.34)
#12
float('12.34')
#12.34
str(1.23)
#'1.23'
str(100)
#'100'
bool(1)
#True
bool('')
#False
print(bool(None))

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))



##################
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(1))


def abs(s):
    if s < 2:
        return 2
    elif s <5:
        return 5
    else :
        return 8

print(abs(10))

#定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来


#######数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x



#######返回多个值的时候 默认返回了tuple其实还是一个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

############
#练习
#ax2 + bx + c = 0的两个解。
def quadratic(a, b, c):
    if a==0 and b!=0:
        return -c/b
    else:
        return (-b+math.sqrt(b**2-4*a*c))/(2*a),(-b-math.sqrt(b**2-4*a*c))/(2*a)

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
