"""
This file has the code to draw a snake which has variables of length, colour, thickness. Everytime a segment value is
asked from the user in a range of 0-500 (checked for its validity). A boundary is drawn for coordinate range of
(-200, -200) to (200, 200). If the snake reaches the boundary it changes its direction and continues to move forward
till the segment turns 0. The snake is drawn under recursion and iteration.
For each movement done by the snake the total length of the snake is given on the screen.

@author Santosh Kumar Nunna (sn7916@rit.edu)
@author Mouna Reddy Kallu (mk9014@rit.edu)
"""
import turtle
import random

def draw_outline(pointer):
    """
    This function is designed to draw the boundary for the snake to move around.
    The outline is drawn in coordinate range of (-200, -200) to (200, 200) and traced back to (0,0).
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :param pointer: turtle object
    :return: None
    """
    pointer.up()
    pointer.goto(-200, 200)
    pointer.down()
    for _ in range(4):
        pointer.forward(400)
        pointer.right(90)
    pointer.up()
    pointer.goto(0,0)
    pointer.setheading(0)

def draw_snake_recursion(pointer, segment, snake_len = 0):
    """
    This function draws the snake in the boundary designed for the given number of segments using recursion.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :param pointer: turtle object
    :param segment: segment value
    :param snake_len: Total length of the snake drawn at the end of function
    :return: None
    """
    if segment == 0:
        print("Snake length: " + str(snake_len))
    else:
        print("Snake length: " + str(snake_len))
        pointer.up()
        len = random.randint(1, 20)
        thick = random.randint(1, 10)
        angle = random.randint(-30, 30)
        colour = random.choice(["blue", "yellow", "cyan", "red","brown"])
        side = random.choice(["right", "left"])
        if side == "right":
            pointer.right(angle)
        else:
            pointer.left(angle)
        pointer.pensize(thick)
        pointer.pencolor(colour)
        pointer.forward(len)
        if not boundary_checker(pointer):
            pointer.back(len)
            if side == "right":
                pointer.right(180)
            else:
                pointer.left(180)
        else:
            pointer.back(len)
        pointer.down()
        pointer.forward(len)
        draw_snake_recursion(pointer, segment-1, snake_len + len)

def draw_snake_iteration(pointer, segment):
    """
    This function is designed to draw the snake in the boundary using iteration for the given number of segments.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :param pointer: turtle object
    :param segment: segments to be drawn
    :return: None
    """
    snake_len = 0
    if segment == 0:
        print("Snake length: 0")
    else:
        while segment > 0:
            pointer.up()
            len = random.randint(1, 20)
            thick = random.randint(1, 10)
            angle = random.randint(-30, 30)
            colour = random.choice(["blue", "yellow", "cyan", "red", "brown"])
            side = random.choice(["right", "left"])
            if side == "right":
                pointer.right(angle)
            else:
                pointer.left(angle)
            pointer.pensize(thick)
            pointer.pencolor(colour)
            pointer.forward(len)
            if not boundary_checker(pointer):
                pointer.back(len)
                if side == "right":
                    pointer.right(180)
                else:
                    pointer.left(180)
            else:
                pointer.back(len)
            pointer.down()
            pointer.forward(len)
            snake_len += len
            print("Snake length: " + str(snake_len))
            segment -= 1



def boundary_checker(pointer):
    """
    This function checks if the snake is out of the boundary or not and returns a boolean value (true) if it goes
    out of boundary.
    :pre: (relative) pos (0,0), heading (east), up
    :post: (relative) pos (0,0), heading (east), up
    :param pointer: turtle object
    :return: boolean value; true if it is out of boundary, false if not out of boundary
    """
    x,y = pointer.pos()
    if (x > -200 and x < 200) and (y > -200 and y < 200):
        return True
    return False


if __name__ == "__main__":
    num_Valid = False
    while not num_Valid:
        segment = int(input("Segment (0-500): "))
        if segment >=0 and segment <=500:
            num_Valid = True
        else:
            print("Segments must be between 0 and 500 inclusive. Try again.")
    turtle_obj = turtle.Turtle()
    turtle_obj.setheading(0)
    turtle_obj.up()
    draw_outline(turtle_obj)
    draw_snake_recursion(turtle_obj, segment)
    to_continue = input("Press Enter to continue to Iterative snake")
    turtle_obj.reset()
    draw_outline(turtle_obj)
    draw_snake_iteration(turtle_obj, segment)
