import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def draw_h(pointer, segments, length):
    if segments == 0:
        pass
    else:
        pointer.right(90)
        pointer.forward(length/2)
        pointer.left(90)
        pointer.forward(length/2)
        draw_h(pointer, segments-1, length/2)
        pointer.backward(length)
        draw_h(pointer, segments - 1, length / 2)
        pointer.forward(length/2)
        pointer.left(90)
        pointer.forward(length)
        pointer.right(90)
        pointer.forward(length/2)
        draw_h(pointer, segments - 1, length / 2)
        pointer.backward(length)
        draw_h(pointer, segments - 1, length / 2)
        pointer.forward(length/2)
        pointer.right(90)
        pointer.forward(length/2)
        pointer.left(90)



if __name__ == "__main__":
    turtle.setworldcoordinates(-WINDOW_HEIGHT/2, -WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH/2)
    turtle.title("the H")
    turtle_obj = turtle.Turtle()
    turtle_obj._tracer(0,0)
    turtle_obj.setheading(90)
    draw_h(turtle_obj, 3, 80)
    turtle_obj._update()
    turtle.done()
