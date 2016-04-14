#-*-coding:utf8-*-

import re
import sys
import requests
import sframe
reload(sys)
sys.setdefaultencoding("utf-8")
import pandas as pd

df = pd.read_csv('zhaopin.csv', encoding = 'utf-8', sep = '\t', header = None)
data = df[8:40]