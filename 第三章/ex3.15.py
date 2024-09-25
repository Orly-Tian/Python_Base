# p78 一年有360天，初始水平值为1.0，以每个月30天计算，在每个月初连续工作10天里，每工作一天水平增加N，
# 该月其他时间内工作与不工作时水平都不增加，请编写程序运算结果填写下表

import numpy as np


def calculate_dayup(dayfactor):
    dayup = 1.0
    for j in range(1, 361):
        if (j % 30) in range(1, 11):
            dayup = dayup * (1 + dayfactor)
    return dayup


dayfactor = np.arange(0.001, 0.011, 0.001)

for i in dayfactor:
    print("%.2f" % calculate_dayup(i))
