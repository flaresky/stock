# -*- coding: utf-8 -*-
# 等额本息，计算每月还款额

nianlilv = 0.13  #年利率
benjin = 10000    #借款金额
month = 12        #借款月数

yuelilv = nianlilv / 12.0
yuehuan = benjin * yuelilv * pow(1+yuelilv, month) / (pow(1+yuelilv, month) - 1)
total_lixi = 0

print "贷款金额： %d"%(benjin)
print "贷款期限： %d个月"%(month)
print "贷款利率： %.2f%%"%(nianlilv*100)
print "每月还款： %.2f"%(yuehuan)
print "-----------------------------------------"
print "期次\t偿还本息\t偿还利息\t偿还本金\t剩余本金"
for i in range(month):
    huanli = benjin * yuelilv
    huanben = yuehuan - huanli
    benjin = benjin - huanben
    total_lixi = total_lixi + huanli
    print "%d\t%.2f\t%.2f\t%.2f\t%.2f"%(i+1, yuehuan, huanli, huanben, benjin)
print "-----------------------------------------"
print "累计支付利息： %.2f"%(total_lixi)
print "累计还款总额： %.2f"%(yuehuan*month)