# -*- coding: utf-8 -*-
import re
import datetime
import utils
import mysqllib
import traceback
from EmailSender import EmailSender

def main():
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    
    today = datetime.datetime.today()
    ts = today.strftime("%Y-%m-%d")
    sql = "select code, name from new_stock where `date`='%s'"%(ts)
    cursor.execute(sql)
    stocks = []
    for (code, name) in cursor:
        stocks.append("%s-%s"%(code, name))
    if len(stocks) > 0:
        ns = "申购新股：%s"%(' '.join([f.encode('utf-8') for f in stocks]))
        es = EmailSender()
        es.send_mail("申购新股", ns)
        es.close()
        utils.print_with_time(ns.decode('utf-8'))
    utils.print_with_time("Done")
    
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    main()