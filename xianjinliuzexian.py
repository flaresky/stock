# -*- coding: utf-8 -*-

jinglirun = 61.8 #净利润
chengzang = ((10, 0.03),(40, 0.03)) #前10年5%增长，然后40年3%增长净利润
chengzang = ((33, 0.05),) #前10年5%增长，然后40年3%增长
lilv = 0.08 #无风险利率

guzi = jinglirun
index = 0
for (year,cz) in chengzang:
    for y in range(year):
        jinglirun = jinglirun * (1 + cz)
        index += 1
        guzi += jinglirun / ((1+lilv) ** index)
print guzi