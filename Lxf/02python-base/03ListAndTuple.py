#Python内置的一种数据类型是列表：list。
# list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael','Bob','Tracy']
print(classmates) #['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
#最后一个元素的取法
print(classmates[len(classmates)-1])
print(classmates[-1])
#倒数第二个  一次类推
print(classmates[-2])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
#默认加在最后一个  append()
classmates.append('admin')
print(classmates) # ['Michael', 'Bob', 'Tracy', 'admin']
#插入指定的位置1 原先依次往后退一个   insert(1,'haifeng')
classmates.insert(1,'haifeng')
print(classmates) #['Michael', 'haifeng', 'Bob', 'Tracy', 'admin']
#删除list末尾的元素，用 pop()
classmates.pop()
print(classmates) # ['Michael', 'haifeng', 'Bob', 'Tracy']
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print(classmates) #['Michael', 'Bob', 'Tracy']
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'haode'
print(classmates) #['Michael', 'haode', 'Tracy']


# list里面的元素的数据类型也可以不同 也可以是一个list
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s) #['python', 'java', ['asp', 'php'], 'scheme']
#那上面的数据可以看做是二维数组
print(p[0]) #asp
print(s[2][0])  #asp



#########
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字
#其实这个tuple就类似是静态变量一样是不能修改的，但是是能读取出来的
classmates = ('ddd',2,True)
print(classmates) #('ddd', 2, True)
print(classmates[1]) #2
t = ()
print(t)
#只有一个元素的时候 必须要加，号
classmates = (1,)
print(classmates[0])
#单单这样这括号就是数学的括号不是一个tuple 如下就是一个数字1
classmates = (1)
classmates = ('1')
print(classmates)
#Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
###############
# 这里要好好理解 其实变的是list 而不是tuple tuple一旦定义那么存储的地方就定死了


##########
# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])




















