# -*- coding: utf-8 -*-
# 国债逆回购提醒
import utils
import time
from EmailSender import EmailSender

notify_price = 5

content = ''
max_price = 0
url = 'https://www.jisilu.cn/data/repo/sz_repo_list/?___t=%d'%(int(time.time()*1000))
jo = utils.fetch_json(url)
for cell in jo['rows']:
    id = cell['id']
    price = float(cell['cell']['price'])
    utils.print_with_time("%s %.2f%%"%(id, price))
    max_price = max(max_price, price)
    if price >= notify_price:
        content = content + "%s %.2f%%\n"%(id, price)
if content != '':
    es = EmailSender()
    es.send_mail("国债逆回购  %.2f%%"%(max_price), content)