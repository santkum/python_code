import turtle

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def rect_rec(pointer, segment, length, width):
    if segment == 0:
        pass
    else:
        for _ in range(2):
            pointer.forward(length)
            pointer.left(90)
            pointer.forward(width)
            pointer.left(90)
        pointer.forward(length/3)
        pointer.left(90)
        pointer.forward(width/3)
        pointer.right(90)
        rect_rec(pointer, segment-1, length/3, width/3)
        pointer.left(90)
        pointer.forward(2*(width/3))
        pointer.right(90)
        pointer.forward(length/3)
        pointer.right(90)
        pointer.forward(width)
        pointer.left(90)
        pointer.backward(2*(length/3))

if __name__ == "__main__":
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_HEIGHT/2, WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.title("draw rectangles")
    turtle_obj = turtle.Turtle()
    turtle_obj.setheading(0)
    rect_rec(turtle_obj, 5, 400, 100)
    turtle.done()