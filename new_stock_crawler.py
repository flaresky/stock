# -*- coding: utf-8 -*-
import re
import datetime
import utils
import mysqllib
import traceback

ds_ptn = re.compile(r".*(\d{2})-(\d{2}).*")
def transform_date(ds):
    res = ds_ptn.search(ds)
    if res is not None:
        month = res.group(1)
        day = res.group(2)
        today = datetime.datetime.today()
        if month >= today.month:
            return "%s-%s-%s"%(today.year, month, day)
        else:
            return "%s-%s-%s"%(today.year+1, month, day)
    return None

def main():
    cnx = mysqllib.get_connection()
    cursor = cnx.cursor()
    url = "http://www.jisilu.cn/jisiludata/newstock.php?qtype=apply"
    jo = utils.fetch_json(url)
    for row in jo['rows']:
        cell = row['cell']
        name = row['id']
        sid = cell['stock_cd']
        apply_dt = transform_date(cell['apply_dt'])
        utils.print_with_time("%s %s %s"%(sid, name, apply_dt))
        
        try:
            keys = ['code', 'name', 'date']
            keys = ["`"+f+"`" for f in keys]
            vals = [sid, name, apply_dt]
            vals = ["'"+f+"'" for f in vals]
            updates = [keys[i]+"="+vals[i] for i in range(0, len(keys))]
        except:
            traceback.print_exc()
            return
        
        sql = "INSERT INTO new_stock (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s"%(', '.join(keys), ', '.join(vals), ', '.join(updates))
#         print sql
        cursor.execute(sql)
        cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == '__main__':
#     transform_date(1)
    main()