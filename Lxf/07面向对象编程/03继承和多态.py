#继承的好处就是自己不用写方法，直接就可以从父那里继承方法和使用方法
#多态
class Animal(object):
    def run(self):
        print('father running...')

class Cat(Animal):
    def run(self):
        print('cat running')

class Dog(Animal):
    def run(self):
        print("dog running...")

cat = Cat()
cat.run()

dog = Dog()
dog.run()


#a、b、c确实对应着list、Animal、Dog这3种类型
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

#看来c不仅仅是Dog，c还是Animal！


# “开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

tor = Tortoise()
tor.run()


#
#多态  子类展示出与父类不同的方法
#














