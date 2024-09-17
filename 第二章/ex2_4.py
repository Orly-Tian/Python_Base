import turtle as t


# 三角形
# for i in range(0, 3):
#     t.left(120)
#     t.forward(200)
# t.done()


# 叠加三角形
for i in range(0, 3):
    t.left(120)
    t.fd(200)

t.left(120)
t.fd(60)
for i in range(0, 3):
    t.fd(60)
    t.left(120)
t.done()
