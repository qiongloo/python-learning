#HTMLParser


#第一步是用爬虫把目标网站的页面抓下来，
# 第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)



parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')


# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，
# 然后尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
#
#

# from urllib import request
# import ssl
#
#
# class MyHTMLParser2(HTMLParser):
#
#     _data = {'data':[]}
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
#
#
#
#
#
# ssl._create_default_https_context = ssl._create_unverified_context
# req = request.Request('https://www.python.org/events/python-events/')
# with request.urlopen(req) as f:
#     _data = f.read().decode('utf-8')
#
#
#
#
# parser = MyHTMLParser()
# parser.feed(_data)






from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re
import json

list=[]
class MyHTMLParser(HTMLParser):
    curtag = ''
    curattrs = None
    def handle_starttag(self, tag, attrs):
        self.curtag = tag
        self.curattrs = attrs
        if tag == 'time':
            if len(attrs)>0:
                if tag == 'time' and 'datetime' in attrs[0]:
                    list[-1]['event_time'] = attrs[0][1]

def handle_endtag(self, tag):
    pass

def handle_startendtag(self, tag, attrs):
    pass

def handle_data(self, data):
    tag = self.curtag
    attrs = self.curattrs
    if tag == 'a' or tag == 'span':
        if len(attrs)>0:
            if 'href' in attrs[0]:
                url = attrs[0][1]
                if re.match(r'^/events/python-events/\d+/$', url):
                    list.append({'event_title':'', 'event_time':'', 'event_location':''})
                    list[-1]['event_title'] += data
            elif 'event-location' in attrs[0]:
                list[-1]['event_location'] += data
    self.curtag = ''
    self.curattrs = None
parser = MyHTMLParser()

url = 'https://www.python.org/events/python-events/'
html = ''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

with request.urlopen(url) as f:
    html = f.read().decode('utf-8')

parser.feed(html)

print(list)
print(len(list))




















