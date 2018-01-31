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

####tuple也是一种list tuple也可以用切片操作，只是操作的结果仍是tuple
####tuple也是一种list tuple也可以用切片操作，只是操作的结果仍是tuple
####字符串'xxx'也可以看成是一种list，每个元素就是一个字符。字符串也可以用切片操作结果仍是字符串
print([1,2,3,4,4][:3]) #[1, 2, 3]
print((1,2,3,4,5)[:3]) #(1, 2, 3)
print('stringAndNew'[:3]) #str
print('stringAndNew'[::3]) #siAN

#各种截取函数（例如，substring）







