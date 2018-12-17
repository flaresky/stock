# -*- coding: utf-8 -*-
import mysqllib
import datetime
import time
import argparse
import settings
import extractor
import utils
import sys
import codecs
import locale

def st_stock(code, verbose, max_pe=1000000):
    code = code.strip()
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    year = datetime.datetime.today().year - settings.avgmgsyYear
    sql = "SELECT AVG(jbmgsy) as avg_jbmgsy from stock_year WHERE `year`>=%d and code=%s GROUP BY code"%(year, code)
    cursor.execute(sql)
    for (tp,) in cursor:
        avg_jbmgsy = tp
        break
    sql = "SELECT mgjzc from stock_year WHERE code=%s ORDER BY `year` DESC LIMIT 1"%(code)
    cursor.execute(sql)
    for (tp,) in cursor:
        mgjzc = tp
        break
    sql = "SELECT name, fieldjp, xj, syl from stock WHERE code=%s"%(code)
    cursor.execute(sql)
    for (name, fieldjp, xj, syl) in cursor:
#         name = utils.pad_str(name, 10)
        try:
            if float(syl) == 0:
                roe = 0
            else:
                roe = float(xj)/float(mgjzc)/syl
            if float(syl) <= max_pe and float(syl) > 0 and float(xj)/float(avg_jbmgsy) < max_pe and float(xj)/float(avg_jbmgsy) > 0:
                utils.print_with_time(u"%s\t%s\t%s\t现价=%s\t平均每股收益=%.3f\t每股净资产=%s\tPE=%.2f\tPE(avg)=%.2f\tPB=%.2f\tROE=%.2f"%(code, name, fieldjp, xj, float(avg_jbmgsy), mgjzc, float(syl), float(xj)/float(avg_jbmgsy), float(xj)/float(mgjzc), roe))
        except:
            if max_pe > 1000:
                utils.print_with_time(u"%s\t%s\t%s\t现价=%s\t平均每股收益=%.3f\t每股净资产=%s\tPE=%.2f"%(code, name, fieldjp, xj, float(avg_jbmgsy), mgjzc, float(syl)))
    if verbose:
        fields = ['year', 'jbmgsy', 'mgjzc', 'mgxjl']
        sql = "SELECT %s from stock_year WHERE `year`>=%d and code=%s order by `year` desc"%(','.join(fields), year, code)
        cursor.execute(sql)
        utils.print_with_time("\t".join(fields))
        for row in cursor:
#             print "\t".join([str(i) for i in row])
            utils.print_with_time("\t".join([str(i) for i in row]))

def st_mystock():
    for code in settings.myStocks:
        st_stock(code)

def st_hangye(hangye):
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    sql = "SELECT code from stock WHERE fieldjp='%s'"%(hangye)
    cursor.execute(sql)
    for (code,) in cursor:
        st_stock(code)

def main():
    parser = argparse.ArgumentParser(description='stock statistics')
    parser.add_argument('-r', '--refresh', required=False, action='store_true', help='refresh stock price')
    parser.add_argument('-v', '--verbose', required=False, action='store_true', help='show verbose')
    parser.add_argument('-s', '--stock_codes', type=str, nargs='*', help='stock codees')
    parser.add_argument('-y', '--hangye', type=str, help='hangye jp')
    parser.add_argument('-f', '--filter', required=False, type=float, help='filter stock by pe')
    parser.add_argument('-m', '--mystock', required=False, type=int, default=0, help='mystock type')
    res = parser.parse_args()
    if res.stock_codes is not None:
        for i in range(len(res.stock_codes)):
            code = res.stock_codes[i]
            if res.refresh:
                if i > 0:
                    time.sleep(settings.sleepTime)
                extractor.extract_stock(code)
            st_stock(code, res.verbose)
    elif res.hangye is not None:
        cnx = mysqllib.get_connection()
        cursor = cnx.cursor()
        sql = "SELECT code from stock WHERE fieldjp='%s'"%(res.hangye)
        cursor.execute(sql)
        for (code,) in cursor:
            if res.refresh:
                extractor.extract_stock(code)
            st_stock(code, res.verbose)
            if res.refresh:
                time.sleep(settings.sleepTime)
    elif res.filter:
        cnx = mysqllib.get_connection()
        cursor = cnx.cursor()
        sql = "SELECT code from stock order by fieldcode"
        cursor.execute(sql)
        for (code,) in cursor:
            st_stock(code, res.verbose, res.filter)
    elif res.mystock is not None:
        cnx = mysqllib.get_connection()
        cursor = cnx.cursor()
        sql = "SELECT code from mystock"
        if res.mystock <> 0:
            sql = sql + " where `type`=%d"%(res.mystock)
        cursor.execute(sql)
        for (code,) in cursor:
            if res.refresh:
                extractor.extract_stock(code)
            st_stock(code, res.verbose)
            if res.refresh:
                time.sleep(settings.sleepTime)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()