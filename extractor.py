import urllib2
import json
import re
import sys
import argparse
import traceback
import mysqllib
import time
import utils
import settings

def extract_stock(code):
    fields = {
              'code' : 'stockcode',
              'name' : 'stockname',
              'fieldcode' : 'fieldcode',
              'fieldname' : 'fieldname',
              'fieldjp' : 'fieldjp',
              'syl' : 'syl',
              'xj' : 'xj',
              }
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    url = "http://stockpage.10jqka.com.cn/spService/%s/Header/realHeader"%(code)
    jo = utils.fetch_json(url)
    if jo is not None:
        try:
            keys = fields.keys()
            vals = ["'"+ (jo[fields[k]] or '')+"'" for k in keys]
            updates = [keys[i]+"="+vals[i] for i in range(0, len(keys))]
        except:
            utils.print_with_time("url=%s"%(url))
            traceback.print_exc()
            return
        
        sql = "INSERT INTO stock (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s"%(', '.join(keys), ', '.join(vals), ', '.join(updates))
#         print sql
        cursor.execute(sql)
        cnx.commit()
    cursor.close()
    cnx.close()

def extract_stock2(code):
    fields = {
              'sjl' : '592920',
              'zsz' : '3541450',
              'ltsz' : '3475914',
              }
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    url = "http://d.10jqka.com.cn/v2/realhead/hs_%s/last.js"%(code)
    data = utils.fetch_url(url)
    data = re.sub(r'quotebridge.*?\((.*)\)', r'\1', data)
    jo = json.loads(data)['items']
    if jo is not None:
        try:
            jo['3541450'] = "%.2f"%(float(jo['3541450']) / 100000000)
            jo['3475914'] = "%.2f"%(float(jo['3475914']) / 100000000)
            keys = fields.keys()
            vals = ["'"+ (jo[fields[k]] or '')+"'" for k in keys]
            keys.append('code')
            vals.append("'%s'"%(code))
            updates = [keys[i]+"="+vals[i] for i in range(0, len(keys))]
        except:
            utils.print_with_time("url=%s"%(url))
            traceback.print_exc()
            return
         
        sql = "INSERT INTO stock (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s"%(', '.join(keys), ', '.join(vals), ', '.join(updates))
#         print sql
        cursor.execute(sql)
        cnx.commit()
    cursor.close()
    cnx.close()

def extract_year(code):
    indexs = {
              1 : 'jbmgsy',
              7 : 'mgjzc',
              13 : 'mgxjl',
              }
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    url = "http://stockpage.10jqka.com.cn/basic/%s/main.txt"%(code)
    jo = utils.fetch_json(url)
#     print data; return
    if jo is not None:
        dmap = {}
        for index in indexs.keys():
            title = jo['title'][index]
            title = '_'.join(title)
            years = jo['year'][0]
            values = jo['year'][index]
            for y in range(0, len(years)):
                year = years[y]
                value = values[y]
                if not dmap.has_key(year):
                    dmap[year] = {}
                dmap[year][indexs[index]] = value
    #             print '%s\t%s\t%s'%(title, year, value)
        for year, ydata in dmap.items():
            fields = indexs.values()
            values = [ydata[f] or '0' for f in fields]
            updates = [fields[i]+"="+values[i] for i in range(0, len(fields))]
    #         print fields
    #         print values
            sql = "INSERT INTO stock_year (code, year, %s) VALUES ('%s', %s, %s) ON DUPLICATE KEY UPDATE %s"%(', '.join(fields), code, year, ', '.join(values), ', '.join(updates))
    #         print sql
            cursor.execute(sql)
        cnx.commit()
    cursor.close()
    cnx.close()

def extract_code(code):
    try:
        extract_stock(code)
    except:
        utils.print_with_time(traceback.format_exc())
    utils.print_with_time("extract_stock %s"%(code))
    time.sleep(settings.sleepTime)
    try:
        extract_stock2(code)
    except:
        utils.print_with_time(traceback.format_exc())
    utils.print_with_time("extract_stock2 %s"%(code))
    time.sleep(settings.sleepTime)
    try:
        extract_year(code)
    except:
        utils.print_with_time(traceback.format_exc())
    utils.print_with_time("extract_year %s"%(code))
    time.sleep(settings.sleepTime)

def extract_mystock():
    for code in settings.myStocks:
        extract_code(code)

def main():
    parser = argparse.ArgumentParser(description='stock extractor')
    parser.add_argument('-a', '--all', required=False, action='store_true', help='refresh all info')
    parser.add_argument('-s', '--stock_codes', type=str, nargs='*', help='stock codees')
    parser.add_argument('-m', '--mystock', required=False, type=int, default=0, help='mystock type')
    res = parser.parse_args()
    if res.stock_codes is not None:
        for i in range(len(res.stock_codes)):
            code = res.stock_codes[i]
            if res.all:
                extract_code(code)
            else:
                extract_stock(code)
                utils.print_with_time("extract_stock %s"%(code))
                time.sleep(settings.sleepTime)
    elif res.mystock is not None:
        cnx = mysqllib.get_connection()
        cursor = cnx.cursor()
        sql = "SELECT code from mystock"
        if res.mystock <> 0:
            sql = sql + " where `type`=%d"%(res.mystock)
        cursor.execute(sql)
        for (code,) in cursor:
            if res.all:
                extract_code(code)
            else:
                extract_stock(code)
                utils.print_with_time("extract_stock %s"%(code))
                time.sleep(settings.sleepTime)
    else:
        parser.print_help()
    

if __name__ == '__main__':
    extract_code('000651'); sys.exit()
    main()