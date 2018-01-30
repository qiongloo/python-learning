#用if语句实现
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

#完整版本 可以用elif做更细致的判断
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

######
# 练习
height = 1.75
weight = 80.5
bmi = weight/(height**2)
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<25:
    print('正常')
elif 25<=bmi<28:
    print ('过重')
elif 28<=bmi<32:
    print ('肥胖')
elif bmi>=32:
    print('严重肥胖')


###########
#for循环输出

#for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
#计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
for x in [0,1,2,3,4,5,6,7,8,9] :
    sum = sum + x
print(sum)


#计算1-100的整数之和 range(5)生成的序列是从0开始小于5的整数
print(range(5))
print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


###########
#while循环输出
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

##########
## 练习
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello,'+x+'!')



####
#break 和 continue
# 提前结束循环，可以用break语句
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)



#####总结
#以上很常规
#if for while 逻辑    break和continue











