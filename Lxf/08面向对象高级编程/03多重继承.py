####多重继承


# MixIn
#
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    def eat(self):
        print('大口大口地吃肉...')

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

print(Dog.__mro__)

##通过__mro__可以看到 他到底的继承怎么来的 打印出所有的父类










