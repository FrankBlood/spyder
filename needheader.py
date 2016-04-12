#-*-coding:utf8-*-
import requests
import re
import sys

#sys.setdefaultencoding("gb18030")
type = sys.getfilesystemencoding()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
html = requests.get('http://www.jikexueyuan.com/course/python/',headers=headers)
html.encoding = 'utf-8'
#print html.text
title = re.findall('900027">(.*?)</a>',html.text,re.S)
print 'The title is fellows:'
for each in title:
    print each
classes = re.findall('cgid="(\d{1,3})">(.*?)</a>',html.text,re.S)
print 'The classes are fellows:'
for each in classes:
    print each
