#struct
#

n = 10240099
print(n & 0xff)
print(n & 0xff00)
print(n & 0xff0000)
print(n & 0xff000000)


#提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
#struct的pack函数把任意数据类型变成bytes：
import  struct
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print(struct.pack('>I',10240099)) #b'\x00\x9c@c'
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80')) #(4042322160, 32896)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))
##(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)


#练习
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
def bmp_info(data):
    return {
        'width': 200,
        'height': 100,
        'color': 24
    }
print(bytes(bmp_data)[:30])
#print(struct.unpack('>IH', bmp_data))

#print(struct.unpack('<ccIIIIIIHH', bmp_data))
def bmp_info(data):
    s = struct.unpack('<ccIIIIIIHH', data[:30])
    print(s)
    return {'width': s[6], 'height': s[7], 'color': s[-1]}

# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')