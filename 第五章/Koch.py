import turtle


turtle.pensize(2)
turtle.pencolor("blue")

# 设置初始位置为
# x = -100
# y = 0
turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()
turtle.speed(0)


def Koch_line(n = 1, len = 120):
    if n == 0:
        turtle.fd(len)
    else:
        # 基本操作,即一阶科赫曲线
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            # 高阶曲线下,每一步操作都要递归完整的四步操作
            Koch_line(n-1, len / 3)


Koch_line(4, 500)

turtle.done()


