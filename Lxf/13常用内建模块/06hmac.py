#Python自带的hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')

# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest()) #fa4ee7d173f2d97ee79022d1a7355bcf




# 练习
#
# 将上一节的salt改为标准的hmac算法，验证用户口令：

# -*- coding: utf-8 -*-
import hmac, random
#print(''.join([chr(random.randint(48, 122)) for i in range(20)]))

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')