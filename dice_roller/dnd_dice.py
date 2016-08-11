# -*- coding:utf-8 -*-

from random import randint
from sys import exit
import re

# 用户输入命令
roll = input('> ')

# 用正则表达式解析用户命令
match = re.search(r'(\d+)([Dd])(\d+)', roll)

# 判断输入语句是否合法——『ndn』模式
if match:
    # 第一个数字，乘数，str
    m = match.group(1)
    # 第二个数字，骰子的面数，int(str)
    n = int(match.group(3))
else:
    print('What do you mean?')
    exit()

# 定义n面骰
def d(n):
    result = randint(1, n)
    print(result)

# 重复投掷
for i in m:
   d(n)