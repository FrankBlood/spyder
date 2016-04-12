import requests
import re
import sys

#sys.setdefaultencoding("gb18030")
type = sys.getfilesystemencoding()

link = 'http://znxyw.org.cn/bencandy.php?fid=12&id=130655'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

content = requests.get(link, headers=headers)
content.encoding = 'GBK'
whole = re.findall('<SPAN class=com_style>\r\n\r\n<div>&nbsp; &nbsp; (.*?)</div><div><br /></div>', content.text, re.S)
print whole[0]