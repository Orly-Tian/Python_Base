import turtle as t
import cv2


img = cv2.imread('webLogo.png')
shape = img.shape
t.colormode(255)
t.tracer(2000)
t.penup()
t.goto(-shape[1] / 2, shape[0] / 2)
for i in range(shape[0]):
    t.pendown()
    for j in range(shape[1]):
        [b, g, r] = img[i][j]
        t.color((r, g, b))
        t.fd(1)
    t.penup()
    t.goto(-shape[1] / 2, shape[0] / 2 - i)
    t.update()
t.done()
