#如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
#类属性 直接在类的下面定义属性就好了



class Student(object):
    name = 'Student'


stu = Student()
print(stu.name)
print(Student.name)

stu.name = 'mc'
print(stu.name)
del stu.name
print(stu.name)


###；练习

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count +1


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')





