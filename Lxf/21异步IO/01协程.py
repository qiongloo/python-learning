###协程，又称微线程，纤程。英文名Coroutine。

#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

#注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。

#
# 协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
#
# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#
#

def consumer():
    r = ''
    while True:
        n = yield r
        if not n :
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n<5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)










def consumer():
    r = None
    while True:
        # 2.consumer通过yield拿到传递的None，yield跳出
        n = yield r
        # 4.从上次跳出的位置，接着往下执行
        if not n:
            return
        print('[CONSUMER] Consuming %s ...' % n )
        r = '200 OK'
        # 6.从这里开始循环，到yield的时候，再跳出来

def produce(c):
    # 1.启动生成器，会跳到consumer
    c.send(None)
    # 3.接着往下执行，产生数据，通过c.send(n)，再切换到consumer
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s ...' % n )
        r = c.send(n)
        # 7.跳出来后，函数返回值是200 OK，所以往下执行，print出200 OK
        print('[PRODUCER Consumer return: %s' % r)
        # 8.从这里开始循环前面的步骤，直到最后
    c.close()

c = consumer()
produce(c)

















