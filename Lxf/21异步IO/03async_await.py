

# async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。

import  asyncio
@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")




async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


async def hello1():
    print("Hello world1!")
    r = await asyncio.sleep(1)
    print("Hello again1!")
async def hello2():
    print("Hello world2!")
    r = await asyncio.sleep(1)
    print("Hello again2!")

# # get EventLoop
# loop = asyncio.get_event_loop()
# # exec coroutine
# loop.run_until_complete(asyncio.wait([hello1(), hello2()]))
# loop.close()







import asyncio


async def wget(host):
    print("wget {}".format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
    writer.write(header.encode("utf-8"))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print("{} header:{}".format(host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()





