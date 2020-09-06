#! /usr/bin/python3

import re
import sys
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
print(title[0], " // ", auther[0], " // ", page[0])
f.close()
