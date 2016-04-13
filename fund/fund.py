# ！python3
# -*- coding:utf-8 -*-

import webbrowser as wbr
import requests as rq
import re

# 下载基金页面代码，并保存为txt。xq-兴全轻资产，hs-华商优势行业
res_xq = rq.get('http://fund.eastmoney.com/163412.html')
playFile_xq = open('fund_xq.txt', 'wb')
for chunk_xq in res_xq.iter_content(100000):
  playFile_xq.write(chunk_xq)

playFile_xq.close

## 华商代码，同上
res_hs = rq.get('http://fund.eastmoney.com/000390.html')
playFile_hs = open('fund_hs.txt', 'wb')
for chunk_hs in res_hs.iter_content(100000):
  playFile_hs.write(chunk_hs)

playFile_hs.close 


# 在txt中用正则表达式查找html代码中的相关语句
htmlCode_xq = open('fund_xq.txt', 'r')
content_xq = htmlCode_xq.read(int(200000))

fundValueRegex = re.compile(r'id="gz_gsz">\d\.\d\d\d\d</span>')
matchList_xq = fundValueRegex.findall(content_xq)

## 华商代码，同上
htmlCode_hs = open('fund_hs.txt', 'r')
content_hs = htmlCode_hs.read(int(200000))

fundValueRegex = re.compile(r'id="gz_gsz">\d\.\d\d\d\d</span>')
matchList_hs = fundValueRegex.findall(content_hs)

# 将匹配到的List，转换成String
matchString_xq = ''.join(matchList_xq)

## 华商代码，同上
matchString_hs = ''.join(matchList_hs)

# 对匹配结果进行二次处理，从中提取数字
numRegex = re.compile(r'\d\.\d\d\d\d')
fundValueList_xq = numRegex.findall(matchString_xq)
fundValue_xq = ''.join(fundValueList_xq)

## 华商代码，同上
fundValueList_hs = numRegex.findall(matchString_hs)
fundValue_hs = ''.join(fundValueList_hs)

print('兴全轻资产 每份额净值 :' + fundValue_xq)
print('华商优势行业 每份额净值 :' + fundValue_hs)

total = round(float(fundValue_xq) *  100940.38 + float(fundValue_hs) * 220322.65, 2)

print('持仓总额  : ' + str(total))

if total < 500000:
  print('亏损:' + str(round(total - 500000, 2)))
else:
  print('盈利:' + str(round(total - 500000, 2)))
