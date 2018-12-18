# -*- coding: utf-8 -*-
import urllib.request
import json
import time
import datetime
import sys
import codecs
import locale
import settings

# sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

def print_with_time(str):
    print(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + ' ')
    print(str)
    sys.stdout.flush()

def fetch_url(url):
    for i in range(settings.urlRetryTimes):
        try:
            data = urllib.request.urlopen(url).read()
            if len(data) > 0:
                return data
        except:
            time.sleep(settings.sleepTime + i)
    return None

def fetch_json(url):
    for i in range(settings.urlRetryTimes):
        try:
            data = urllib.request.urlopen(url).read()
            jo = json.loads(data)
            return jo
        except:
            time.sleep(settings.sleepTime + i)
    return None

def pad_str(s, length):
    if len(s) >= length:
        return s
    return ' ' * (length - len(s)) + s

if __name__ == '__main__':
    print(fetch_url('https://www.jisilu.cn/jisiludata/newstock.php?qtype=apply'))