#map()函数
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def  f(x):
    return x * x
r = map(f,[1,2,3,4,5,6])
print(list(r)) #[1, 4, 9, 16, 25, 36]

print(list(map(str,[1,2,3,4,5,6]))) #['1', '2', '3', '4', '5', '6']

#reduce函数
#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x,y):
    return x + y
reduce(add,[1,2,3,4,5])


def char2num(s):
    digits =  {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(list(map(char2num, '134567')))

#str转换为int的函数：
#1
def fn(x, y):
    return x * 10 + y

print(reduce(fn,map(char2num,'12345')))

#2
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return  reduce(fn,map(char2num,s))
print(str2int('23313131'))


####
##练习
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return str(name[0:1]).upper()+str(name[1:]).lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
   def tt(x,y):
       return x * y
   return  reduce(tt,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def str2num(n):
        return  DIGITS[n]
    def fn(x,y):
        return x*10 + y
    L = s.split('.')
    return reduce(fn,map(str2int,L[0]))+reduce(fn,map(str2int,L[1]))/(10**len(L[1]))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
print('123')

####函数filter()
#和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))
print([x for x in [1, 2, 4, 5, 6, 9, 10, 15] if x % 2 == 1])

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    s = str(n)
    s2 = s[::-1]
    return s==s2

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


#排序算法
#sorted()函数就可以对list进行排序：
print(sorted([4,32,5,7,21,1])) #[1, 4, 5, 7, 21, 32]
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21],key=abs)) #[5, 9, -12, -21, 36]

#字符串排序 按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print(sorted(['bob', 'about', 'Zoo', 'Credit'])) #['Credit', 'Zoo', 'about', 'bob']
#忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) #['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)) #['Zoo', 'Credit', 'bob', 'about']


##练习
## 假设我们用一组tuple表示学生名字和成绩： 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return  t[0]
L2 = sorted(L, key=by_name)
print(L2)

#再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)



