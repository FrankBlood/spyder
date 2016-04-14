#-*-coding:utf8-*-

import re
import sys
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'http://123.sogou.com/shwz/jianfei.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
html = requests.get(url, headers = headers)

s = open('jianfei.csv', 'w')
everyclass = re.findall('<a target="_blank" title=.*? href="(.*?)">(.*?)</a>', html.text, re.S)#减肥
for each in everyclass:
    print each[0], each[1]
    s.writelines(str(each[0]) + '\t' + str(each[1]) + '\n')
s.close()

# everyclass = re.findall('<a target="_blank" title=.*? href="(.*?)">(.*?)</a>', html.text, re.S)#健康
# for each in everyclass:
#     print each[0], each[1]
#     s.writelines(str(each[0]) + '\t' + str(each[1]) + '\n')
# s.close()


# everyclass = re.findall('<a target="_blank" title=.*? href="(.*?)">(.*?)</a>', html.text, re.S)#搜狗房产
# for each in everyclass:
#     print each[0], each[1]
#     s.writelines(str(each[0]) + '\t' + str(each[1]) + '\n')
# s.close()

# everyclass = re.findall('<a target="_blank" title=.*? href="(.*?)">(.*?)</a>', html.text, re.S) #搜狗股票
# for each in everyclass:
#     #print each[0], each[1]
#     if str(each[1]) == '更多证券公司>>':
#         Url = str(each[0])
#         content = requests.get(Url, headers = headers)
#         whole = re.findall(r'<a class=\'url_fav\' href=\'(.*?)\'.*?>(.*?)</a>', content.text, re.S)
#         for link in whole:
#             print link[0], link[1]
#             s.writelines(str(link[0]) + '\t' + str(link[1]) + '\n')
#     else:
#         s.writelines(str(each[0]) + '\t' + str(each[1]) + '\n')
# s.close()


# everyclass = re.findall('<a(.*?)>(.*?)</a>', html.text, re.S)#搜狗新闻
# for each in everyclass:
#     #print each[0], each[1]
#     #s.writelines(str(each[0]) + '\t' + str(each[1]) + '\n')
#     if re.match(r'.*?=\'(.*?)\' title.*',str(each[0])):
#         m = re.match(r'.*?=\'(.*?)\' title.*',str(each[0]))
#         print m.group(1), each[1]
#         if re.match('http://.*?', m.group(1)):
#             s.writelines(str(m.group(1))+ '\t' + str(each[1]) + '\n')
#         else:
#             Url = 'http://123.sogou.com'+str(m.group(1))
#             content = requests.get(Url, headers = headers)
#             whole = re.findall(r'<a class.*? href=\'(.*?)\' .*?>(.*?)</a>', content.text, re.S)
#             for link in whole:
#                 print link[0], link[1]
#                 s.writelines(str(link[0]) + '\t' + str(link[1]) + '\n')
# s.close()

#everyclass = re.findall('<a target=".*?" title=".*?" href="(.*?)">(.*?)</a>', html.text, re.S) #搜狗招聘
# everyclass = re.findall(r'<a target="_blank".*?href="(.*?)"*>(.*?)</a>', html.text, re.S) #百度

#搜狗招聘
# for each in everyclass:
#     if re.match('^招聘 - .*?', str(each[1])):
#         Url = 'http://123.sogou.com'+str(each[0])
#         print Url
#         content = requests.get(Url, headers = headers)
#         whole = re.findall('<a target=".*?" title=".*?" href="(.*?)">(.*?)</a>', content.text, re.S)  # 搜狗新闻
#         for link in whole:
#             print link
#             s.writelines(str(link[0]) + '\t' + str(link[1]) + '\n')
#     else:
#         print each
#         s.writelines(str(each[0])+ '\t' + str(each[1]) + '\n')
# s.close()

#保存爬取内容
# f = open('category_text.txt', 'w')
# f.writelines(str(html.text))
# f.close()