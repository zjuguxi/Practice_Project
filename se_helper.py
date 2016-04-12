# -*- coding:utf-8 -*-
#! python3

import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.baidu.com/s?wd=nihao%20mandarin')
