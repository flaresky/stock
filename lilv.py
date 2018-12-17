# -*- coding: utf-8 -*-
#为期10个月，每月定投金额，负数表示取现，计算年化收益率
biandong = [1000, 1500, 800, 1000, 1000, -700, 900, 1000, 2000, 1500]
biandong = [1000] * 10

class nian_lilv_calculator:
    __input_money = []
    def calc(self, input_money, final_value):
        self.__input_money = input_money
        yue_lilv = self.__calc_recurse(-1, 1, final_value)
        nian_lilv = pow(1 + yue_lilv, 12) - 1
        return nian_lilv
    
    def __calc_recurse(self, minval, maxval, final_value):
        lilv = (minval + maxval) / 2.0
        val = self.__calc_final_value(lilv)
        if abs(final_value - val) < 0.01:
            return lilv
        if val < final_value:
            return self.__calc_recurse(lilv, maxval, final_value)
        else:
            return self.__calc_recurse(minval, lilv, final_value)
    
    def __calc_final_value(self, x):
        total = 0
        length = len(self.__input_money)
        for i in range(0, length):
            total += self.__input_money[i] * pow(1+x, length-i)
        return total

if __name__ == '__main__':
    calculator = nian_lilv_calculator()
    print calculator.calc(biandong, 11000)