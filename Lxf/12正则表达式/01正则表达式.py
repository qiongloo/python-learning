###正则表达式
# \d可以匹配一个数字
# \w可以匹配一个字母或数字
# .可以匹配任意字符
# *表示任意个字符（包括0个）
# 用+表示至少一个字符
# 用?表示0个或1个字符
# 用{n}表示n个字符
# 用{n,m}表示n-m个字符

# [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
# A|B可以匹配A或B
# ^表示行的开头，^\d表示必须以数字开头
# $表示行的结束，\d$表示必须以数字结束



#re模块
#强烈建议使用Python的r前缀，就不用考虑转义的问题了
#s = r'ABC\-001'    对应的正则表达式字符串不变：'ABC\-001'

#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')


import re

print(re.match(r'^\d{3}-\d{3,8}$','011-1111'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))



#切分字符串
print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


#分组 正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$','010-123456')
print(m)

print(m.group(0)) #010-123456
print(m.group(1))
print(m.group(2))
#注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。


t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m.groups()) #('19', '05', '30')



######贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups()) #('102300', '')

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

print(re.match(r'^(\d+?)(0*)$', '102300').groups()) #('1023', '00')




#预编译
#如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：



re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())



###练习
#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：

def is_valid_email(addr):
   re_mail = re.compile(r'^[a-zA-z0-9][a-zA-z0-9\_\.]*@[a-zA-z0-9\_]+\.[a-zA-z0-9\_]+$')
   return re_mail.match(addr)



#print(is_valid_email('someone@gmail.com'))

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

###练习
def name_of_email(addr):
    re_name_of_name = re.compile(r'<*([\w\s]*)>*[\s\w]*@[a-zA-z0-9\_]+\.[a-zA-z0-9\_]+$')
    ad = re_name_of_name.match(addr)
    if ad:
        return ad.group(1)
    else:
        return ad
print(name_of_email('<Tom Paris> tom@voyager.org'))


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')















