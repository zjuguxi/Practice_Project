# -*- coding:utf-8 -*-
#! python3

import requests
from bs4 import BeautifulSoup

res_baidu = requests.get('https://www.baidu.com/s?wd=nihao%20mandarin')

code_baidu = open('baidu.html', 'w')
code_baidu.write(res_baidu.text)
code_baidu.close()

soup = BeautifulSoup(open('baidu.html'))

print(soup)
