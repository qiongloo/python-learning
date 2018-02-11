##XML解析


#DOM vs SAX
# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# 在Python中使用SAX解析XML非常简洁，
# 通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了



# <a href="/">python</a>
# 会产生3个事件：
#
# start_element事件，在读取<a href="/">时；
#
# char_data事件，在读取python时；
#
# end_element事件，在读取</a>时。

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)



xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)




# 练习
# 请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取天气预报：
import time
class DefaultSaxHandler2(object):
    data = {'city':None,'forecast':[]}
    def start_element(self, name, attrs):
        if name =='yweather:location' and 'city' in attrs:
            self.data['city'] = attrs['city']
        elif name == 'yweather:forecast' and 'date' in attrs and 'high' in attrs and 'low' in attrs:
            self.data['forecast'].append(
                {'date': time.strftime('%Y-%m-%d',time.strptime(attrs['date'], '%d %b %Y')), 'high': attrs['high'],
                 'low': attrs['low']})

    def end_element(self, name):
       # print('sax:end_element: %s' % name)
        pass

    def char_data(self, text):
       # print('sax:char_data: %s' % text)
        pass

    def get_data(self):
        return self.data

# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request
def parseXml(xml_str):
    handler = DefaultSaxHandler2()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)
    return handler.get_data()

    #
    # print(xml_str)
    # return {
    #     'city': '?',
    #     'forecast': [
    #         {
    #             'date': '2017-11-17',
    #             'high': 43,
    #             'low' : 26
    #         },
    #         {
    #             'date': '2017-11-18',
    #             'high': 41,
    #             'low' : 20
    #         },
    #         {
    #             'date': '2017-11-19',
    #             'high': 43,
    #             'low' : 19
    #         }
    #     ]
    # }
    #


# 测试:
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
print(result)
assert result['city'] == 'Beijing'




