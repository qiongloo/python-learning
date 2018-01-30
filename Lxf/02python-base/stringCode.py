#字符串和编码
#Python 3版本中，字符串是以Unicode编码的
print('包含中文的str')
#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6588')


#Python对bytes类型的数据用带b前缀的单引号或双引号表示
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore'))

##len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'))
print(len('中文'.encode('utf-8')))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#占位符
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('hello, %s' %'world')
print('hello, %s you have %d' %('world',1))
#%s永远起作用，它会把任何数据类型转换为字符串
print('hello, %s you have %s' %('world',1))
#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('hello, %s %%' %'world')
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


####
#Python 3的字符串使用Unicode，直接支持多语言。
#当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。


