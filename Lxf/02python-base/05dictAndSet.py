#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
# 使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#写入
d['Adam'] = 67
print(d['Adam'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Thomas' in d)

#用方法获取数值，不存在的默认为None也可以指定数值后面的-1 因为上面的用[]不存在的时候会报错
print(d.get('Thomas'))  #None
print(d.get('Thomas', -1)) #-1

#pop  不存在的时候是会报错的
d.pop('Bob')
print(d)

#dict是用空间来换取时间的一种方法。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

###############
#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print(s)
#会去掉重复的数值
s = set([1, 1, 2, 2, 3, 3])
print(s)
#不会反复的添加
s.add(4)
print(s)
s.add(4)
print(s)
#remove(key)删除key
s.remove(4)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

d = {(1, 2, 3):33}
print(d[(1, 2, 3)])

#tuple中有list是不能做为key 但是没有list的时候是可以用作key的
# d = {(1, [2, 3]):33}
# t = [2,3]
# d = {(1, t):33}
# print(d[(1, [2, 3])])




