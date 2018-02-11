

#chardet 字符编码(有问题)
import  chardet

print(chardet.detect(b'Hello, world!'))


data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))


data = '哈哈哈sdaf afd'.encode('gbk')
print(chardet.detect(data))










