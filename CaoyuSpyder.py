import re
import requests
import sys

#sys.setdefaultencoding("utf-8")

hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
html = requests.get('http://znxyw.org.cn/list.php?fid=12',headers = hea)
html.encoding = 'GBK'

class spider(object):
    def __init__(self):
        print u'开始爬取内容。。。'

    def changepage(self, url, total_page = 1497):
        now_page = int(re.search('page=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page + 1):
            link = re.sub('page=\d+', 'page=%s' % i, url, re.S)
            page_group.append(link)
        return page_group

    def getsource(self,url,head):
        html = requests.get(url,head)
        html.encoding = 'GBK'
        return html.text


    def geteveryclass(self, source):
        everyclass = re.findall(r'<a href="(bencandy.php.*? )target="_blank">', html.text, re.S)
        content = []
        for each in everyclass:
            m = re.match('(.*?)\" title=\'(.*?)\'', each)
            # content.append(m.group(2),m.group(1))
            print m.group(1), m.group(2)

    def getinfo(self, eachclass):
        info = {}
        info['title'] = re.search('target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        info['content'] = re.search('</h2><p>(.*?)</p>', eachclass, re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>', eachclass, re.S)
        info['classtime'] = timeandlevel[0]
        info['classlevel'] = timeandlevel[1]
        info['learnnum'] = re.search('"learn-number">(.*?)</em>', eachclass, re.S).group(1)
        return info

    def saveinfo(self, classinfo):
        f = open('info.txt', 'a')
        for each in classinfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classtime:' + each['classtime'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum'] + '\n\n')
        f.close()

if __name__ == '__main__':
    classinfo = []
    url = 'http://znxyw.org.cn/list.php?fid=12&page=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}
    CaoyuSpider = spider()
    all_links = CaoyuSpider.changepage(url)
    for link in all_links:
        print u'正在处理页面：' + link
        html = CaoyuSpider.getsource(link, headers)
        everyclass = CaoyuSpider.geteveryclass(html)
        for each in everyclass:
            info = CaoyuSpider.getinfo(each)
            classinfo.append(info)
    CaoyuSpider.saveinfo(classinfo)

print html.text