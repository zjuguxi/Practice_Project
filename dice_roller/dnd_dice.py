# -*- coding:utf-8 -*-

from random import randint
from sys import exit
import re

# 用户输入命令
roll = input('> ')

# 用正则表达式解析用户命令
match = re.search(r'(\d+)([Dd])(\d+)', roll)

# 判断输入语句是否合法——『ndn』格式
if match:
    # 第一个数字，乘数，str
    m = int(match.group(1))
    # 第二个数字，骰子的面数，int(str)
    n = int(match.group(3))
else:
    print('What do you mean?')
    exit()

# 骰子的每个结果都放入一个list，初始为空
dice = []

# 定义n面骰
def d(n):
    return randint(1, n)
# 重复投掷
for i in range(m):
   result = d(n)
   dice.append(result)
   print(result)

print('和为: ', sum(dice))

dice.remove(min(dice))
print('去掉一个最小值，其余求和：', sum(dice))