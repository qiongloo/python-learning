#本节IO编程都是同步模式
# import time
# print(time.localtime())
# print(time.time())

# 2015-04-24
# print(time.strftime('%Y-%m-%d', time.localtime()))
# # 1429857836.0
# print(time.mktime(time.localtime()))
# print(time.strptime('2017.2.6','%Y.%m.%d'))

# import time
# #当前时间
# now_time = time.mktime(time.strptime(time.strftime('%Y.%m.%d', time.localtime()),'%Y.%m.%d'))
# print(now_time) #1486310400.0
# #输入的时间
# input_time = time.mktime(time.strptime('2017.2.6','%Y.%m.%d'))
# print(input_time) #31536000.0
# #时间差
# during =  now_time - input_time
# print(during) # 31536000.0
# format_during = during/(24*60*60)
# print(format_during) #365.0



#计算时间
import time

# 任意输入一个年月日，计算距离今天几年几月几日。
# 要求：
# 使用函数，可复用
# 输入格式：1920.3.28
# 年份范围：1700-2018，超出提示
# 一年按照365天，一月按照30天计算。

#计算输入的时间到今天的时间差（天）

# def calculateTime(input_time):
#     try:
#         s = input_time.split('.')
#         if len(s)!=3:
#             raise Exception
#             return
#         if not 1700 <= int(s[0]) <= 2018:
#             print('输入的时间必须在1700~2018之间')
#             input_time = input('请重新输入你想输入的时间(格式2016.1.2):')
#             calculateTime(input_time)
#             return
#         _temp_input_time = time.strptime(input_time,'%Y.%m.%d')
#     except Exception as e:
#         print('时间格式错误！')
#         input_time = input('请重新输入你想输入的时间(格式2016.1.2):')
#         calculateTime(input_time)
#         return
#
#     now_time = time.mktime(time.strptime(time.strftime('%Y.%m.%d', time.localtime()),'%Y.%m.%d'))
#     input_time_rel = time.mktime(_temp_input_time)
#     during = (now_time - input_time_rel)/(24*60*60)
#     #print(during)
#     year = int(during/365)
#     month = int(during/30-year*12)
#     day = int(during-year*12*30-month*30)
#     print('输入的时间距离今天:%d年%d月%d天' %(year,month,day))
#     return
#
#
# input_time = input('请输入你想输入的时间(格式2016.1.2):')
# calculateTime(input_time)

# if not 1700 <= int(time.strftime('%Y', _temp_input_time)) <= 2018:
#     print('输入的时间必须在1700~2018之间')
#     input_time = input('请重新输入你想输入的时间(格式2016.1.2):')
#     calculateTime(input_time)
#     return








#常规的读取
# try:
#     f=open('/Users/billy/Desktop/1.txt', 'r',encoding="utf-8")
#     print(f.read())
# finally:
#     if f:
#         f.close()

#另外一种读取方式 更加简洁 然后不用close()
# with open('/Users/billy/Desktop/1.txt', 'r',encoding="utf-8")  as f :
#     print(f.read())

##一行一行的读取
# with open('/Users/billy/Desktop/1.txt', 'r',encoding="utf-8")  as f :
#     for line in f.readlines():
#         print(line.strip())

#也可以是用read(size)



####二进制打开方式
f = open('/Users/billy/Desktop/1.txt', 'rb')
print(f.read())

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理
#f = open('/Users/billy/Desktop/1.txt', 'r', encoding="utf-8",errors='ignore')





#写文件
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# f = open('/Users/billy/Desktop/1.txt', 'w')
# f.write('hello world')
# f.close()

#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）
#传入'a'以追加（append）模式写入
# with open('/Users/billy/Desktop/1.txt', 'a') as f:
#     f.write('Hello, world!')




####练习
#请将本地一个文本文件读为一个str并打印出来：

fpath = r'/Users/billy/Desktop/1.txt'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)









