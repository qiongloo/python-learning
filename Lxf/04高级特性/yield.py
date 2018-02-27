#
#
#
#


def h():
    print('Wen Chuan')
    m = yield 5  # Fighting!
    print(m)
    d = yield 12
    print('We are together!')

c = h()
# c.next()  #相当于c.send(None)
# c.send('Fighting!')  #(yield 5)表达式被赋予了'Fighting!'
c.send(None)
c.send('Fighting!')
c.send(33)
# print('We will never forget the date', c.m, '.', c.d)





