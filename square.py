import turtle
from math import sqrt

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
minimize = 11


def draw_basic(pointer, length):
    colours = ["red", "violet"]
    pointer.color(colours[length % 2])
    pointer.down()
    pointer.begin_fill()
    for _ in range(4):
        pointer.forward(length)
        pointer.left(90)
    pointer.end_fill()


def draw_square(pointer, segments, length):
    if segments == 0:
        pass
    else:
        draw_basic(pointer, length)
        pointer.up()
        pointer.left(45)
        pointer.forward(sqrt((minimize / 2) ** 2 + (minimize / 2) ** 2))
        pointer.right(45)
        draw_square(pointer, segments - 1, length - minimize)


if __name__ == "__main__":
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.title("Squares")
    turtle_obj = turtle.Turtle()
    turtle_obj._tracer(0, 0)
    turtle_obj.setheading(0)
    draw_square(turtle_obj, 10, 100)
    turtle.done()
