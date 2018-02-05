####Python内置的@property装饰器就是负责把一个方法变成属性调用的：


#raise 引发一个异常 且它们应是Error或Exception类的子类。
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score is not int')
        if value <0 or value >100:
            raise ValueError('score must between 100 ~ 200')
        self._score = value

s = Student()
s.set_score(80)
print(s.get_score())

##s.set_score(800)


#修改成property
#把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value,int):
            raise ValueError('score is not int')
        if value <0 or value >100:
            raise ValueError('score must between 100 ~ 200')
        self._score = value

s = Student()
s.score = 80
print(s.score)



#练习
#请利用@property给一个Screen对象加上width和height属性，
# 以及一个只读属性resolution

class Screen(object):

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return  self._height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



