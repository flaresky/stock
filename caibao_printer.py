# -*- coding: utf-8 -*-
import sys
import json
import traceback

import mysqllib
from constants import *
import settings

stock_code = settings.extract_stock_code

def print_caibao(stock_code, tb, from_year, end_year):
    sql = "select `year`, %s from stock_caibao where `code`='%s' and `year`>=%d and `year`<=%d"%(tb, stock_code, from_year, end_year)
    dbres = mysqllib.fetch(sql)
    caibaos = {}
    for row in dbres:
        caibaos[int(row['year'])] = json.loads(row[tb])
#     print caibaos
    title_row = ['title']
    for year in range(from_year, end_year+1):
        title_row.append(str(year))
    print '\t'.join(title_row)
    for f,nov in TABLE_FIELDS[tb]:
        print_this_row = False
        row = [f]
        for year in range(from_year, end_year+1):
            if f in caibaos[year]:
                row.append('%f'%caibaos[year][f])
                print_this_row = True
            else:
                row.append('0')
        if print_this_row:
            print '\t'.join(row)


# print_caibao(stock_code, 'zcfzb', 2010, 2015)
# print_caibao(stock_code, 'lrb', 2010, 2015)
print_caibao(stock_code, 'xjllb', 2010, 2015)