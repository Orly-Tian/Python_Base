import turtle


def Koch(n, len):
    if n == 0:
        turtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            Koch(n - 1, len / 3)


def main():
    turtle.up()
    turtle.goto(-250, 150)
    turtle.pendown()
    turtle.color("blue")
    turtle.speed(0)

    len = 500
    n = 3
    for i in [0, -120, -120]:
        turtle.left(i)
        Koch(n, len)
    turtle.done()


if __name__ == "__main__":
    main()

