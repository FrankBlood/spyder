#-*-coding:utf8-*-
import requests
import re
import sys
import numpy as np
import pandas as pd

#sys.setdefaultencoding("gb18030")
#type = sys.getfilesystemencoding()
url = 'http://znxyw.org.cn/list.php?fid=12&page=1'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

now_page = int(re.search('page=(\d+)', url, re.S).group(1))
page_group = []
for i in range(now_page, 2):
    link = re.sub('page=\d+', 'page=%s' % i, url, re.S)
    page_group.append(link)

for link in page_group:
    html = requests.get(link, headers=headers)
    html.encoding = 'GBK'
    everyclass = re.findall(r'<a href="(bencandy.php.*? )target="_blank">', html.text, re.S)
    website = []
    name = []
    message = []
    for each in everyclass:
        m = re.match('(.*?)\" title=\'(.*?)\'', each)
        content_link = 'http://znxyw.org.cn/'+m.group(1)
        content = requests.get(content_link, headers=headers)
        content.encoding = 'GBK'
        whole = re.findall('<SPAN class=com_style>\r\n\r\n<div>&nbsp; &nbsp; (.*?)</div><div><br /></div>', content.text, re.S)
        for s in whole:
            message.append(s)
            print s
        print content_link,m.group(2)

        website.append(content_link)
        name.append(m.group(2))
    df = pd.DataFrame(website,name)
    df.to_csv('memeda.csv')
