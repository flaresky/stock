# -*- coding: utf-8 -*-
import re
import datetime
import utils
import traceback
from EmailSender import send_mail

ds_ptn = re.compile(r".*(\d{2})-(\d{2}).*")
def transform_date(ds):
    res = ds_ptn.search(ds)
    if res is not None:
        month = res.group(1)
        day = res.group(2)
        today = datetime.datetime.today()
        if int(month) >= int(today.month):
            return "%s-%s-%s"%(today.year, month, day)
        else:
            return "%s-%s-%s"%(today.year+1, month, day)
    return None

def main():
    today = datetime.datetime.today()
    ts = today.strftime("%Y-%m-%d")
    ts = "2018-12-18"
    stocks = []
    url = "http://www.jisilu.cn/jisiludata/newstock.php?qtype=apply"
    jo = utils.fetch_json(url)
    for row in jo['rows']:
        cell = row['cell']
        name = row['id']
        sid = cell['stock_cd']
        apply_dt = transform_date(cell['apply_dt'])
        if apply_dt == ts:
            stocks.append("%s-%s"%(sid, name))
    
    if len(stocks) > 0:
        ns = "申购新股：%s"%(' '.join(stocks))
        send_mail("申购新股", ns)
        utils.print_with_time(ns)
    utils.print_with_time("Done")

if __name__ == '__main__':
    main()