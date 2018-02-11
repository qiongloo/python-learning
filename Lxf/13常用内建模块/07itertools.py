#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
import itertools


#count()会创建一个无限的迭代器
natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# 注意字符串也是序列的一种
cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)


ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)


#takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x <=10,natuals)
print(list(ns))





#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器

for c in itertools.chain('ABCD','12345'):
    print(c)


#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))


#忽略大小写
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# 练习
# 计算圆周率可以根据公式：



#lambda 遇到false的时候就会停下来

# -*- coding: utf-8 -*-
import itertools

def pi(N):
        ' 计算pi的值 '
        # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
        pi = itertools.count(1, 2)
        # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
        pi = itertools.takewhile(lambda x: x <= 2 * N - 1, pi)
        # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
        zf = itertools.cycle([+4, -4])
        # step 4: 求和:
        return sum(next(zf) / next(pi) for x in range(N))


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
print(pi(1000000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')










