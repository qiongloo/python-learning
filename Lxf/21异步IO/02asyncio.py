##############
##############
#############



#
# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
#
# asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
#

import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用asyncio.sleep(1)
    r = yield  from asyncio.sleep(1)
    # print('ddfd')
    # b = yield 'dfsdfsdf'
    # print(b)
    print("Hello again!")

#
#
# loop = asyncio.get_event_loop()
#
# loop.run_until_complete(hello())
#
# loop.close()












import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        # yield from asyncio.sleep(1)
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()








































