#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等



import  hashlib

md5 = hashlib.md5()
md5.update('how to user md5 in python hashlib'.encode('UTF-8'))
print(md5.hexdigest())

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib4?'.encode('utf-8'))
print(md5.hexdigest())


#另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
print(sha1.hexdigest())
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


#根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return  md5.hexdigest()

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    if calc_md5(password)==db[user]:
        return True
    else:
        return False


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')







