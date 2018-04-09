#接口就是WSGI：Web Server Gateway Interface。

#WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
# 我们来看一个最简单的Web版本的“Hello, web!”



def  application(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    #[b'<h1>Hello, web!</h1>']

    return [body.encode('utf-8')]

from wsgiref.simple_server import make_server

httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()






































