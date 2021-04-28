# -*- coding: utf-8 -*-

# @File         : demo.py
# @Date         : 2021-04-01
# @Author       : Liuker
# @girlFriend   : Penny

import csv
import os
from bs4 import BeautifulSoup


def parse_html(html_file):
    csv_header = ('委托编号', '委托名称', '委托方', '委托类型', '集团跟进人', '国家/地区', '委托时间', '状态')
    csv_body = list()

    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f)
        table = soup.select('tbody')[0]

        row_list = table.find_all(class_='ant-table-row')
        for row in row_list:
            td_list = row.select('td')[1:]

            columns = list()
            for td in td_list:
                columns.append(td.get_text())

            csv_body.append(tuple(columns))

    # 写入CSV
    file_name = 'data.csv'
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerows(csv_body)
        f.flush()
        print('success')


def main():
    parse_html('Alibaba法律服务工作台.html')


if __name__ == '__main__':
    main()
