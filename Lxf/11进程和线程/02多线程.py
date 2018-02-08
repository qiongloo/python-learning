#Python的标准库提供了两个模块：_thread和threading，
# _thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块



import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# #t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


#t = threading.Thread(target=loop,name='loopThread')

###线程锁

import  time, threading

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


#当数字特别大的时候 会导致数据混乱 没有同步
def run_thread(n):
    for i in range(1000000):
        change_it(n)

lock = threading.Lock()
#加一把锁然后释放掉
def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)




import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()







