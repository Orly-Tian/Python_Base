from turtle import *
from random import *
from math import *


class Tree:
    def __init__(self):
        # 设置画布大小
        setup(1000, 700)
        # 设置背景颜色
        bgcolor(1, 1, 1)
        ht()
        # 画笔速度
        speed(0)
        tracer(1, 100)
        pu()
        backward(100)
        left(90)
        backward(300)

    def tree(self, n, l):
        pd()
        # 阴影效果
        t = cos(radians(heading() + 45)) / 8 + 0.25
        pencolor(t, t, t)
        pensize(n / 1.2)
        forward(l)
        if n > 0:
            # 右分支偏转角度
            b = random() * 15 + 10
            # 左分支偏转角度
            c = random() * 15 + 10
            # 下一个分支的长度
            d = l * (random() * 0.25 + 0.7)
            # 右转一定角度，画右分支
            right(b)
            self.tree(n - 1, d)
            # 左转一定角度，画右分支
            right(b + c)
            self.tree(n - 1, d)
            # 转回来
            right(c)
        else:
            # 画叶子
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n, n * 0.8, n * 0.8)
            fillcolor(n, n * 0.8, n * 0.8)
            begin_fill()
            circle(3)
            left(90)
            end_fill()

            # 添加0.3倍的飘落叶子
            if random() > 0.7:
                pu()
                # 飘落
                t = heading()
                an = -40 + random() * 40
                setheading(an)
                dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
                forward(dis)
                setheading(t)
                # 画叶子
                pd()
                right(90)
                n = cos(radians(heading() - 45)) / 4 + 0.5
                pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
                fillcolor(n, n * 0.8, n * 0.8)
                begin_fill()
                circle(2)
                left(90)
                end_fill()
                pu()
                # 返回
                t = heading()
                setheading(an)
                backward(dis)
                setheading(t)
                # pass
        pu()
        backward(l)


def main():
    tree = Tree()
    tree.tree(12, 100)
    done()


if __name__ == "__main__":
    main()
