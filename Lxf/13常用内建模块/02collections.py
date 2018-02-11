#collections是Python内建的一个集合模块，提供了许多有用的集合类

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))

#如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
Circle = namedtuple('Circle',['x','y','r'])
circle = Circle('1','2','3')
print(circle.x)
print(circle.y)
print(circle.r)




#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，
# 这样就可以非常高效地往头部添加或删除元素。
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)




#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import  defaultdict
dd = defaultdict(lambda :'N/A')
dd['kk'] = 'abc'
print(dd['kk'])
print(dd['K1'])




#OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
#如果要保持Key的顺序，可以用OrderedDict

from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)  #{'a': 1, 'b': 2, 'c': 3}
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od) #OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od.keys())
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od)



#OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
###这段代码先放着
from collections import OrderedDict
class LastUpdatedOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderDict,self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:',last)
        if containsKey:
            del self[key]
            print('set:',(key, value))
        else:
            print('add:',(key, value))
        OrderedDict.__setitem__(self, key, value)


#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数

from collections import  Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)






















