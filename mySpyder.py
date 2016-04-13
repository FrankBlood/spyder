#-*-coding:utf8-*-
import re
import sys

import requests

#import pandas as pd
reload(sys)
sys.setdefaultencoding("utf-8")
# How to use mySpyder.
url = 'http://znxyw.org.cn/list.php?fid=12&page=1'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

now_page = int(re.search('page=(\d+)', url, re.S).group(1))
page_group = []
for i in range(now_page, 2):
    link = re.sub('page=\d+', 'page=%s' % i, url, re.S)
    page_group.append(link)

f = open('memeda.csv', 'w')

for link in page_group:
    html = requests.get(link, headers=headers)
    html.encoding = 'GBK'
    everyclass = re.findall(r'<a href="(bencandy.php.*? )target="_blank">', html.text, re.S)

    for each in everyclass:
        m = re.match('(.*?)\" title=\'(.*?)\'', each)
        content_link = 'http://znxyw.org.cn/'+m.group(1)
        content = requests.get(content_link, headers=headers)
        content.encoding = 'GBK'
        whole = re.findall('<SPAN class=com_style>\r\n\r\n<div>&nbsp; &nbsp; (.*?)</div><div><br /></div>', content.text, re.S)
        name = m.group(2)

        for s in whole:
            f.writelines(str(content_link) + '\t' + str(name) + '\t' + str(s) + '\n')
            print s

        print content_link,name
        name.encode(encoding= 'GBK')
f.close()
