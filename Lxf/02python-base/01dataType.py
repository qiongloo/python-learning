#语句以冒号结尾的，缩进代码看做是代码块   但是没讲缩进是几个空格，我们约定使用4个空格缩进
#缩进注意的是复制的时候 很容易出问题
# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)

############
## 浮点型
print(3.1415926)
print(1.2e-5)
#16进制的表达
print(0xff00)
#转义符的运用
print('I\'m OK.')
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')
#默认不转义
print(r'\\\t\\')
#换行使用\n 或者使用'''...'''来进行表示多行
print('''a\n
b
c''')
print('a '
      'a')
#加r  不转义
print(r'''a \n
b
c''')


##########
## 布尔值
#使用 and or
True
False
3 > 2
print(3 > 2)
print(3 > 2 or 1 > 3)
print(3 > 4 and 3 > 1)

# age = input()
# if age >= 18:
#     print('adult')
# else:
#     print('teenager')


##########
#变量名必须是大小写英文、数字和_的组合，且不能用数字开头
t_007 = 'T007'
print(t_007)
#同一个变量可以反复赋值，而且可以是不同类型的变量 所以python是动态语言
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)


#一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据
#这里注意b指向的是a的数据
a = 'ABC'
b = a
a = 'XYZ'
print(b)


############
#常量
PI=3.1415926
#两个整数恰好整除，结果也是浮点数
print(10 / 3)
#取整数部分
print(10 // 3)
#求余
print(10 % 3)

#Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。
#Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
#
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
s5 = '''Hello,
Lisa!'''
print(s3)
print(s4)
print(s5)
#r只是不转义 而'''...'''也是一张表达和''一样
