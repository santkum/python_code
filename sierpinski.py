import turtle
import random

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

class Sierpinski:

    def __init__(self, turtle_obj):
        turtle.setworldcoordinates(-WINDOW_HEIGHT / 2, -WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2)
        turtle.title("Sierpinski triangles")
        self.pointer = turtle_obj
        self.pointer.speed(10)
        self.pointer.up()
        self.pointer.setheading(0)

    def draw_triangle(self, length, dress):
        self.pointer.color(dress)
        self.pointer.begin_fill()
        for _ in range(3):
            self.pointer.down()
            self.pointer.forward(length)
            self.pointer.left(120)
        self.pointer.end_fill()

    def draw_recursion(self, segments, length):
        colors = ['blue','green','white','yellow', 'violet']
        if segments <= 0:
            pass
        else:
            dr = colors[segments%5]
            self.draw_triangle(length, dr)
            self.draw_recursion(segments - 1, int(length / 2))
            self.pointer.up()
            self.pointer.forward(length)
            self.pointer.left(120)
            self.draw_recursion(segments - 1, int(length / 2))
            self.pointer.up()
            self.pointer.forward(length)
            self.pointer.left(120)
            self.draw_recursion(segments - 1, int(length / 2))
            self.pointer.up()
            self.pointer.forward(length)
            self.pointer.left(120)


if __name__ == "__main__":
    turtle_ob = turtle.Turtle()
    turtle_ob._tracer(0,0)
    draw_sierpinski = Sierpinski(turtle_ob)
    draw_sierpinski.draw_recursion(5, 200)
    turtle.done()