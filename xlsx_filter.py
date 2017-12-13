from openpyxl import load_workbook
from collections import defaultdict
import csv
import codecs
from itertools import islice

wb = load_workbook(filename='clients_data_2.xlsx')
ws = wb.get_sheet_by_name('Sheet1')

rows = ws.rows

# 行迭代
content = []
for row in rows:
    line = [col.value for col in row]
    content.append(line)

row_count = 0

phone_set = set()
data = []
num = 1


def get_chunks(data, SIZE):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}


def create_csv(list_of_rows, num):
    headers = ["姓名", "电话", "地址", "单价", "课程", "老师", "是否加微信", "是否报班", "备注"]
    with codecs.open("{}.csv".format(num), "w", 'utf_8_sig') as f:
        # f.write(codecs.BOM_UTF8)
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(list_of_rows)


if __name__ == '__main__':
    clients_dict = defaultdict(list)
    for i, row in enumerate(content):

        # 跳过第一行
        if row_count == 0:
            row_count += 1
            continue
        row_count += 1
        phone = row[1]
        clients_dict[phone].append(row)

    clients_chunks_generator = get_chunks(clients_dict, 35)

    file_count = 1
    for dct in clients_chunks_generator:
        clients_list = []
        for phone, info in dct.items():
            for row in info:
                clients_list.append(row)

        create_csv(clients_list, file_count)
        file_count += 1
