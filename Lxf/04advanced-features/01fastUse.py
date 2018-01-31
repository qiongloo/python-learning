###########切片
##取一个list或tuple的部分元素是非常常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前3个元素，用一行代码就可以完成切片(包含前面不包含后面)
#不包括索引3。即索引0，1，2
print(L[0:3])
#第一个索引是0，还可以省略
print(L[:3])
print(L[1:3])
print(L[-2:])
#-1代表倒数第一个
print(L[-2:-1])
###随机数字列表
L = list(range(100))
#前11-20个数
print(L[10:20])
#前10个数，每两个取一个
print(L[:10:2])
#所有数，每5个取一个
print(L[::5])
#显示所有的数据
print(L[:])

# [::-1]——从头到尾，将数组反转，返回[6, 5, 4, 3, 2]
# [-1::-2]——从尾到头，每个一个元素，选择一个元素，返回[6, 4, 2]
#说明：没有第3个参数时，切片只能从左向右，此时若第一个参数大于等于第二个参数，则返回空数组
#说明：第三个参数<0时，切片方向可以被改变，此时没有上述限制


####tuple也是一种list tuple也可以用切片操作，只是操作的结果仍是tuple
####tuple也是一种list tuple也可以用切片操作，只是操作的结果仍是tuple
####字符串'xxx'也可以看成是一种list，每个元素就是一个字符。字符串也可以用切片操作结果仍是字符串
print([1,2,3,4,4][:3]) #[1, 2, 3]
print((1,2,3,4,5)[:3]) #(1, 2, 3)
print('stringAndNew'[:3]) #str
print('stringAndNew'[::3]) #siAN
print('stringAndNew'[3])
#其他语言各种截取函数（例如，substring）
print(len(''))
##越界的时候 返回空 ''
print(''[0:1])
print('dddd'+'   '[0:0])
#练习
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
# def trim(s):
#     start = 0
#     end = len(s)
#     n=0
#     while n<end:
#         if s[n]==' ':
#             start += 1;
#         else:
#             break
#         n += 1
#     # if start==end:
#     #     return ''
#     n=len(s)-1
#     while n>-1:
#         if s[n] == ' ':
#             end -= 1
#         else:
#             break
#         n -= 1
#     # print(start)
#     # print( end)
#     # if start==end:
#     #     return s[start]
#     return s[start:end]


# def trim(s):
#     i = 0
#     j = len(s)
#     while i !=j and s[i] == ' ':
#         i=i+1
#     while i !=j and s[j-1] == ' ':
#         j=j-1
#     return s[i:j]


def trim(s):
    while s[0:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[0:-1]
    return s

print( trim('  8  ') )
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


#print('ddd\"\"ddd')
################
# 迭代
###只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

#dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
for value in d.values():
    print(value)
# 1
# 2
# 3
#字符串也是可迭代对象
for ch in 'acddd':
    print(ch)
# a
# c
# d
# d
# d

#如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable)) #False


##########for循环下标问题
##Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print(i,value)
print(enumerate(['A','B','C']))

for x,y in [(1,1),(2,3),(3,9)]:
    print(x,y)

for t in [(1,1),(2,3),(3,9)]:
    print(t)

####练习
#请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    x = len(L)
    if x<=0:
        return  (None, None)
    min = L[0]
    max = L[0]
    for s in L:
        if min > s:
            min = s
        if max < s:
            max = s
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


####################
# 列表生成式
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1,11):
    L.append(x * x)
print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x * x for x in range(1,11)])
print(list(x * x for x in range(1,11)))
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0]) #[4, 16, 36, 64, 100]
#还可以使用两层循环，可以生成全排列
print([m + n for m in 'FJF' for n in 'qwe'] ) #['Fq', 'Jq', 'Fq', 'Fw', 'Jw', 'Fw', 'Fe', 'Je', 'Fe']

#三层和三层以上的循环就很少用到
#列出上级目录下的所有文件和目录名
import os
print([d for d in os.listdir('../')]) #['Lxf.iml', '01fisrt-process', '04advanced-features', '03function', '02python-base']

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)
#列表生成式也可以使用两个变量来生成list：
print([k + '=' + v for k,v in d.items()]) #['x=A', 'y=B', 'z=C']

#最后把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L]) #['hello', 'world', 'ibm', 'apple']


####
#练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ s.lower() for s in L1 if isinstance(s,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')













