# 2024/9/26
# PTA：https://pintia.cn/problem-sets/1838922159297183744/exam/problems/type/7?problemSetProblemId=1838940437398753281&page=0

from math import *

a, b, c = (input().split(" "))
a = int(a)
b = int(b)
c = int(c)

x, y, z = (input().split(" pi/"))
x = pi/int(x[3:])
y = pi/int(y)
z = pi/int(z)

V = (1/6)*a*b*c * sqrt(1 - cos(x)**2 - cos(y)**2 - cos(z)**2 + (2*cos(x)*cos(y)*cos(z)))
print("%.2f" % V)

