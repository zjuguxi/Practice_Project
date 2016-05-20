# -*- coding:utf-8 -*-

## 电脑要先安装python3
## 随后在命令行中执行 pip install pandas

## 首先，将excel文档转为csv格式（我mac电脑打开excel有点问题）；
## 然后，将要去重的部分，粘贴到去重列下面；
## 再后，将下面代码的中文部分，按需求改成英文；
## 最后，在命令行中执行 python miner_deng.py
## （注意：在操作命令行时，要进入原文件所在目录下，脚本自动生成的新文件也会保存在同一目录下。）


import pandas as pd

workbook = '原文件名.csv'
new_workbook = '新文件名.csv'

df = pd.read_csv(workbook, low_memory = False)
new_df = df.drop_duplicates(subset = '要去重的列名称，必须英文', keep = False)
new_df.to_csv(new_workbook)