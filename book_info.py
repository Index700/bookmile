#! /usr/bin/python3

import re
import sys
import datetime


def now_time():
    dt_now = datetime.datetime.now()
    if dt_now.day < 10:
        day = str(0) + str(dt_now.day)
    date = str(dt_now.year) + str(dt_now.month) + str(day)
    return date
    
file = sys.argv[1]
# path = '/tmp/url_data'
# path = ''
# path = '/tmp/science_his'
f = open(file)
content = f.read()
book = re.findall(r'<meta name=\"title\" content.*',content)[0]
title = re.findall(r'content=".*?(.*?)\/\/',book)
auther = re.findall(r'content=".*?\/\/ (.*?)\/\/',book)
page = re.findall(r'<span>(.*?ページ)</span>',content)
# print(book)

date = now_time()

print(title[0], " // ", auther[0], " // ", page[0], " // ", date)
f.close()
