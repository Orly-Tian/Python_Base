# 斐波那契数列
# https://pintia.cn/problem-sets/1856738036110544896/exam/problems/type/7?problemSetProblemId=1856740882218434564&page=0

n = int(input())
num1 = 0
num2 = 1

print("%d %d " % (num1, num2), end="")

num = 1
for i in range(1, n):
    num1 = num1 + num2
    num2 = num1 + num2
    if num1 <= n:
        print("%d " % num1, end="")
    if num2 <= n:
        print("%d " % num2, end="")
print("")
