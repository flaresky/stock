# -*- coding: utf-8 -*-
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if a > b:
    tmp = a
    a = b
    b = tmp
nianhua = pow(1 + (b - a) / 2.0 / a, 365) - 1
nianhua = nianhua * 100
print "套利收益 %.2f%%"%(nianhua)