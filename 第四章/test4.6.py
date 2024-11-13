# 羊车门问题描述：
# 有3扇关闭的门，一扇门后停着汽车，另外两扇门后是山羊，主持人知道每扇门后是什么。
# 参赛者首先选择一扇门。在开启它之前，主持人会从另外两扇门中打开一扇门，露出门后的山羊。
# 此时，允许参赛者更换自己的选择。请问，参赛者更换选择后，能否增加猜中汽车的机会？通过设计并编写程序验证，并给出自己的解释。
# (The sheep door has 3 closed door, a door parked car, another two door is a goat, the host knows every door.
# What is the first choice of the contestants in the open door. Before it, the moderator will open a door from
# the other two doors, exposes the goat after. At this time, allow the participants change their choice.
# Please choose the contestants after replacement, can increase the chance of guessing car?
# Please through design and program verification, and gives his own interpretation.)

import random


x = [1, 2, 3]
testNum = 100000
count = 0

for i in range(testNum):
    ans = random.choice(x)
    guess = random.choice(x)
    if ans == guess:
        count += 1
print(count / testNum)

count = 0
for i in range(testNum):
    x = [1, 2, 3]
    ans = random.choice(x)
    guess = random.choice(x)
    # 在选择之外的两个门主持人选一项
    x.remove(guess)
    zhuchi = random.choice(x)
    # 主持人必定选中的是羊
    if zhuchi != ans:
        # 更改选择，即不选主持人开过的门，也不选原来的选择
        x.remove(zhuchi)
        guess = x[0]
        count += 1
print(count / testNum)


