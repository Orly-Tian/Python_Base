# p78 一年有365天，初始水平值为1.0，每工作一天水平增加N，不工作时水平不下降，
# 一周连续工作5天，请编写程序运算结果填写下表

import numpy as np


def calculate_dayup(dayfactor):
    dayup = 1.0
    for j in range(1, 365):
        if not ((j % 7) in [6, 0]):
            dayup = dayup * (1 + dayfactor)
    return dayup


dayfactor = np.arange(0.001, 0.011, 0.001)

for i in dayfactor:
    print("%.2f" % calculate_dayup(i))
