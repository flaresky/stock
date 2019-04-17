# -*- coding: utf-8 -*-
import re
import datetime
import utils
import traceback
from EmailSender import send_mail

notify_rate = 55

def main():
    global notify_rate
    today = datetime.datetime.today()
    ts = today.strftime("%Y-%m-%d")
#     ts = "2019-04-19"
    stocks = []
    url = "https://www.jisilu.cn/data/cbnew/pre_list/?___jsl=LST___t"
    jo = utils.fetch_json(url)
    for row in jo['rows']:
        cell = row['cell']
        apply_dt = cell['apply_date']
        pma_rt = 100
        if 'pma_rt' in cell and cell['pma_rt'] is not None:
            pma_rt = float(cell['pma_rt'])
        if apply_dt == ts and pma_rt >= notify_rate and cell['cb_type'] == u'可转债':
            stocks.append("%s-%s-%.2f%%"%(cell['bond_nm'], cell['apply_cd'], pma_rt))
    
    if len(stocks) > 0:
        ns = "申购可转债：%s"%(' '.join(stocks))
        send_mail("申购可转债", ns)
        utils.print_with_time(ns)
    utils.print_with_time("Done")

if __name__ == '__main__':
    main()