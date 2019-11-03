import turtle
import math

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def draw_hex(pointer, length):
    pointer.down()
    for _ in range(6):
        pointer.forward(length)
        pointer.left(60)
    pointer.up()

def draw_hex_star(pointer, length):
    draw_hex(pointer, length)
    pointer.left(30)
    cross = length * math.sqrt(3)
    pointer.down()
    for _ in range(3):
        pointer.forward(cross)
        pointer.left(120)
    pointer.right(30)
    pointer.forward(length)
    pointer.left(150)
    for _ in range(3):
        pointer.forward(cross)
        pointer.right(120)
    pointer.up()
    pointer.forward(cross/3)
    pointer.right(120)

def draw_2_hex_stars(pointer, length):
    draw_hex(pointer, length)
    for _ in range(2):
        pointer.left(30)
        cross = length * math.sqrt(3)
        pointer.down()
        for _ in range(3):
            pointer.forward(cross)
            pointer.left(120)
        pointer.right(30)
        pointer.forward(length)
        pointer.left(150)
        for _ in range(3):
            pointer.forward(cross)
            pointer.right(120)
        pointer.up()
        pointer.forward(cross / 3)
        pointer.right(120)
        length = length/math.sqrt(3)

def draw_2_bulls_eye(pointer, length):
    draw_hex(pointer, length)
    for _ in range(2):
        pointer.left(30)
        cross = length * math.sqrt(3)
        pointer.down()
        for _ in range(3):
            pointer.forward(cross)
            pointer.left(120)
        pointer.right(30)
        pointer.forward(length)
        pointer.left(150)
        for _ in range(3):
            pointer.forward(cross)
            pointer.right(120)
        pointer.up()
        pointer.forward(cross / 3)
        pointer.right(150)
        draw_circle(pointer, cross / 3)
        pointer.left(30)
        length = length / math.sqrt(3)

def draw_circle(pointer, radius):
    pointer.down()
    pointer.circle(radius)

def draw_bulls_eye_rec(pointer, depth, length, area=0):
    colours = ['blue', 'green']
    if depth <=0:
        print("Area of the green region: " + str(area))
        pass
    else:
        draw_hex_star(pointer, length)
        pointer.right(30)
        pointer.color(colours[depth%2])
        pointer.begin_fill()
        draw_circle(pointer, length/math.sqrt(3))
        pointer.end_fill()
        pointer.left(30)
        if colours[depth%2] == 'green':
            area1 = math.pi * ((length/math.sqrt(3))**2)
            draw_bulls_eye_rec(pointer,depth-1, length/math.sqrt(3), area + area1)
        elif colours[depth%2] == 'blue' and area > 0:
            area1 = math.pi * ((length / math.sqrt(3)) ** 2)
            draw_bulls_eye_rec(pointer, depth - 1, length / math.sqrt(3), area - area1)
        else:
            area1 = math.pi * ((length / math.sqrt(3)) ** 2)
            draw_bulls_eye_rec(pointer, depth - 1, length / math.sqrt(3), area)


if __name__ == "__main__":
    turtle.setworldcoordinates(-WINDOW_HEIGHT/2, -WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/2)
    turtle.title("Bullseye")
    turtle_obj = turtle.Turtle()
    turtle_obj._tracer(0, 0)
    turtle_obj.setheading(0)
    draw_bulls_eye_rec(turtle_obj, 6, 100)
    turtle_obj._update()
    turtle.done()