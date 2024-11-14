# 求素数
# https://pintia.cn/problem-sets/1856738036110544896/exam/problems/type/7?problemSetProblemId=1856740882218434566&page=0

prime = []

for i in range(2, 1001):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)


for i in range(0, len(prime)):
    print("{:<5}".format(prime[i]), end="")
    if (i + 1) % 10 == 0:
        print("")

