##类的属性是可以随便赋值的


#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score



bart = Student('Bart Simpson', 59)

#以上就不能直接访问__name
#print(bart.__name)
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：
print(bart._Student__name)

#使用方法访问私有的变量
print(bart.get_name())

#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，
# 所以，不能用__name__、__score__这样的变量名。




####练习


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return  self.__gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
