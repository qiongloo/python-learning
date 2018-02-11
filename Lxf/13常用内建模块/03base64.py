##
# #Base64是一种用64个字符来表示任意二进制数据的方法
##

#Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示
#要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉

import base64

base64.b64encode(b'binary\x00string')
print(base64.b64encode(b'binary\x00string')) #b'YmluYXJ5AHN0cmluZw=='
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw==')) #b'binary\x00string'


#由于标准的Base64编码后可能出现字符+和/，
# 在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')) #b'abcd--__'
print(base64.urlsafe_b64decode('abcd--__')) #b'i\xb7\x1d\xfb\xef\xff'



# 练习
# 请写一个能处理去掉=的base64解码函数：
import base64

def safe_base64_decode(s):
    if isinstance(s,bytes):
        s_str = s.decode('UTF-8')
    else:
        s_str = str(s)
    l = len(s_str)
    ss = l%4
    for x in range(ss):
        s_str += '='
    s_str_2 = s_str.encode('UTF-8')
    return  base64.b64decode(s_str_2)

# print(type(b'YWJjZA'))
# print(type('YWJjZA'))

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')


print(str(10*'='))
s= 's2s'
print(s+str((-len(s)%4)*'='))







