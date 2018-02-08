#把变量从内存中变成可存储或传输的过程称之为序列化

#pickle.dumps()方法把任意对象序列化成一个bytes
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))


#pickle.dumps()方法把任意对象序列化成一个bytes
#pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('/Users/billy/Desktop/2.txt','wb')
#f.write(b'1')
pickle.dump(d,f)
f.close()


#pickle.loads()方法反序列化出对象
f = open('/Users/billy/Desktop/2.txt','rb')
dd = pickle.load(f)
f.close()
print(dd)





####json和python的转换

#Python对象到JSON格式的转换
import json

d = dict(name='haode', age=1, gender=1)
print(json.dumps(d))

#把JSON反序列化为Python对象
#用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))




#JSON进阶

#dict对象可以直接序列化为JSON的{}，
# 不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
class Student(object):
    def __init__(self, name='', age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob',20,100)
# print(json.dumps(s))


#指定序列化的方式
def stu2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s,default=stu2dict))


#偷个懒，把任意class的实例变为dict
print(json.dumps(s,default=lambda obj:obj.__dict__))


#如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))



###练习
#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)
# print(s)
# s = json.dumps(obj,ensure_ascii=False)
# print(s)

#print(Student().dict)
print(type(s))
print(s.__dict__)
# print(s.dict)


#定义一个
def MyJsonLoads(cls, jsonStr):
    clsDict = cls.__dict__
    jsonDict = json.loads(jsonStr)
    className = str(type(cls))[str(type(cls)).find('.') + 1:-2]
    #eval转化为可执行的表达式
    newObj = eval(className + '()')
    for key in clsDict:
        setattr(newObj, key, jsonDict[key])
        return newObj

s = MyJsonLoads(Student(),'{"name":"123","age":16,"score":1}')
print(s.name)



class Teacher(object):
    # slots = ('name', 'age')
    __slots__ = ('name','age')
    def __init__(self,name, age):
        self.name = name
        self.age = age




t = Teacher('Michael',80)
t.name = 'Michael'
t.age = 80
#print('序列化 slots 修饰的类：', json.dumps(t, default=lambda obj:obj.__dict__))
print('序列化 slots 修饰的类：', json.dumps(t, default=lambda obj:obj.__init__))
#slots 修饰的 class，不具有 dict 属性！






