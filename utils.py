# -*- coding: utf-8 -*-
import urllib2
import json
import time
import datetime
import sys
import codecs
import locale
import settings
import mysqllib

# sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

def print_with_time(str):
    print datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + ' ',
    print str
    sys.stdout.flush()

def fetch_url(url):
    for i in range(settings.urlRetryTimes):
        try:
            data = urllib2.urlopen(url).read()
            if len(data) > 0:
                return data
        except:
            time.sleep(settings.sleepTime + i)
    return None

def fetch_json(url):
    for i in range(settings.urlRetryTimes):
        try:
            data = urllib2.urlopen(url).read()
            jo = json.loads(data)
            return jo
        except:
            time.sleep(settings.sleepTime + i)
    return None

def pad_str(s, length):
    if len(s) >= length:
        return s
    return ' ' * (length - len(s)) + s

def get_stock_name_by_code(code):
    sql = "select name from stock where code=%s"%(code)
    res = mysqllib.fetch_one(sql)
    return res['name']

if __name__ == '__main__':
    print get_stock_name_by_code('000651')