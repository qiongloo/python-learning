###操作文件和目录

####

#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
import os
print(os.name) #posix

print(os.uname())


##操作系统中定义的环境变量，全部保存在os.environ这个变量
print(os.environ)
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
## 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/Users/billy/Desktop/', 'testdir'))
#创建目录
# os.mkdir('/Users/billy/Desktop/2')
#删除目录
#os.rmdir('/Users/billy/Desktop/2')

#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串

#直接去拆字符串，而要通过os.path.split()函数
print(os.path.split('/Users/michael/testdir/file.txt'))
#os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))


#重命名和删除文件
# os.rename('test.txt', 'test.py')
# os.remove('test.py')



#shutil模块提供了copyfile()的函数

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

##############
###练习作业###
##############

#作业1.利用os模块编写一个能实现dir -l 输出的程序
import os
import time

def dir_l(path ='.'):
    print('最后修改时间\t\t\t\t大小\t\t\t文件名')
    print('-----------------------------------------------')
    for f in os.listdir(path):
        fsize = os.path.getsize(f)
        st=os.stat(f)  #stat调用
        mtime = time.strftime('%Y-%m-%d %H:%M',time.localtime(st.st_mtime))
        #localtime():格式化时间戳(最后一次修改的时间)为本地的时间
        #strftime():接收以时间元组,并返回以可读字符串表示的当地时间,格式由参数format决定
        print('%s\t\t%05d B\t\t%s' % (mtime,fsize , f))

dir_l()

#作业2.能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
def show(strs,path = '.'):
    for f in os.listdir(path):
        if os.path.isfile(f) and f.find(strs)>-1:
                print(os.path.abspath(f))
        if os.path.isdir(f):
            show(strs, os.path.abspath(f))

show('Strin')

#递归实现法：遇到文件夹用递归实现查找
def findFile(str,path='.'):
    for f in os.listdir(path):
        fPath = os.path.join(path,f)
        if os.path.isfile(fPath) and str in f:
            print(fPath)
        if os.path.isdir(fPath):
            findFile(str,fPath)
        #注意isfile(fpath)和isdir(fpath)的参数默认为当前目录，
        #写相对路径或绝对路径，不要只写个文件名，避免递归查询时
        #找不到子目录的文件

findFile('Strin')





