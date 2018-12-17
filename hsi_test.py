# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta
from lilv import nian_lilv_calculator
import mysqllib

from_date = date(2001, 1, 1)
end_date = date(2016, 6, 1)
dingtou_money = 3000
pe_config = (10, 14) #pe配置，9以下定投，10以上全部卖掉，9-10之间买回卖掉的
g_raise_step = 0.1
g_sell_step = 0.05
yue_fuli = 0.003#现金年利率，3.6%左右

ACTION_NULL = 0
ACTION_BUY = 1
ACTION_SELL = 2

def get_next_month_date(d):
    if d.month == 12:
        return date(d.year+1, 1, d.day)
    else:
        return date(d.year, d.month+1, d.day)

def get_pe_by_date(d):
    while True:
        d = d - timedelta(days=1)
        sql = "select pe from hsi_pe where `date`='%s'"%(str(d));
        db_res = mysqllib.fetch_one(sql)
        if db_res is not None:
            return db_res['pe']

def get_point_by_date(d):
    while True:
        sql = "select close from hsi_history where `date`='%s'"%(str(d));
        db_res = mysqllib.fetch_one(sql)
        if db_res is not None:
            return db_res['close']
        d = d + timedelta(days=1)

def strategy1(): #每涨10%卖出5%
    cur_date = from_date
    total_month = 0
    total_in = 0
    fen_e = 0
    yu_e = 0
    shizhi = 0
    sell_index = 0
    sell_base = 0
    sell_step = 0
    sell_fene = 0
    pe1 = pe_config[0]
    pe2 = pe_config[1]
    input_money = []
    print 'date\tpe\tpoint\tsell_point\taction\tmoney\t总投入\t余额\t份额\t总市值'
    while cur_date < end_date:
        pe = get_pe_by_date(cur_date)
        point = get_point_by_date(cur_date)
        action = ACTION_NULL
        sell_point = sell_base + sell_index * sell_step
        cur_money = 0
        yu_e = yu_e * (1 + yue_fuli)
        if pe > pe2:
            if sell_index == 0:
                sell_base = point
                sell_step = point * g_raise_step
                sell_fene = fen_e * g_sell_step
            sell_point = sell_base + sell_index * sell_step
            if point >= sell_point:
                sell_index += 1
                if fen_e > 0:
                    as_fene = min(fen_e, sell_fene)
                    fen_e -= as_fene
#                     cur_money = - point * as_fene
                    yu_e += point * as_fene
                    action = ACTION_SELL
        elif pe < pe1:
            action = ACTION_BUY
            sell_index = 0
#             buy_money = 1.0 * dingtou_money * pe1 / pe
            buy_money = 1.0 * dingtou_money
#             cur_money = buy_money
            if yu_e >= buy_money:
                yu_e -= buy_money
            else:
                total_in += buy_money - yu_e
                cur_money = buy_money - yu_e
                yu_e = 0
            fen_e += buy_money * 1.0 / point
        input_money.append(cur_money)
        shizhi = fen_e * point
        print "%s\t%s\t%s\t%.2f\t%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f"%(cur_date, pe, point, sell_point, action, cur_money, total_in, yu_e, fen_e, shizhi)
        
        cur_date = get_next_month_date(cur_date)
        total_month += 1
    calculator = nian_lilv_calculator()
    nianhua_lilv = calculator.calc(input_money, shizhi+yu_e)
    print "total_month=%d, total_in=%d, yue=%.2f, shizhi=%.2f, nianhua=%.4f%%"%(total_month, total_in, yu_e, shizhi, nianhua_lilv*100)
    print len(input_money)

def strategy2(): #每月卖出5%
    cur_date = from_date
    total_month = 0
    total_in = 0
    fen_e = 0
    yu_e = 0
    shizhi = 0
    sell_index = 0
    sell_base = 0
    sell_step = 0
    sell_fene = 0
    pe1 = pe_config[0]
    pe2 = pe_config[1]
    input_money = []
    print 'date\tpe\tpoint\tsell_point\taction\tmoney\t总投入\t余额\t份额\t总市值'
    while cur_date < end_date:
        pe = get_pe_by_date(cur_date)
        point = get_point_by_date(cur_date)
        action = ACTION_NULL
        sell_point = sell_base + sell_index * sell_step
        cur_money = 0
        yu_e = yu_e * (1 + yue_fuli)
        if pe > pe2:
            if sell_index == 0:
                sell_base = point
                sell_step = point * g_raise_step
                sell_fene = fen_e * 0.03
            sell_index += 1
            as_fene = min(fen_e, sell_fene)
            fen_e -= as_fene
            yu_e += point * as_fene
            action = ACTION_SELL
        elif pe < pe1:
            action = ACTION_BUY
            sell_index = 0
#             buy_money = 1.0 * dingtou_money * pe1 / pe
            buy_money = 1.0 * dingtou_money
#             cur_money = buy_money
            if yu_e >= buy_money:
                yu_e -= buy_money
            else:
                total_in += buy_money - yu_e
                cur_money = buy_money - yu_e
                yu_e = 0
            fen_e += buy_money * 1.0 / point
        input_money.append(cur_money)
        shizhi = fen_e * point
        print "%s\t%s\t%s\t%.2f\t%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f"%(cur_date, pe, point, sell_point, action, cur_money, total_in, yu_e, fen_e, shizhi)
        
        cur_date = get_next_month_date(cur_date)
        total_month += 1
    calculator = nian_lilv_calculator()
    nianhua_lilv = calculator.calc(input_money, shizhi+yu_e)
    print "total_month=%d, total_in=%d, yue=%.2f, shizhi=%.2f, nianhua=%.4f%%"%(total_month, total_in, yu_e, shizhi, nianhua_lilv*100)
    print len(input_money)

if __name__ == '__main__':
    strategy2()