"""
Snowflake.py
This function has the ability to draw a snowflake depending on the users depth input. It draws a 3 line snowflake at an
angle turn of 60 degrees. Depending on the depth a snowflake will be added at the end of each flake. This is designed
using the recursion feature. Every time a new snowflake is started drawing the turtle changes its colour based on the
remainder output of the number of colours.

@author: Santosh Kumar Nunna (sn7916@rit.edu)
@author: Mouna Reddy Kallu (mk9014@rit.edu)

"""
import turtle

def drawSnowFlake(turtle_obj, depth, flake_length):
    """
    This function is designed to draw the snowflake as per users depth requirements.
    Every new snowflake has a reduced length which is 1/3rd of its original length.
    :pre: turtle is penup and facing east
    :post: turtle is penup and facing east
    :param turtle_obj: turtle object
    :param depth: depth indicates number of snowflakes which is entered by the user
    :param flake_length: flake length
    :return: None
    """
    angle = 60
    colours = ["violet", "green", "grey"]
    if depth == 0:
        pass
    else:
        for _ in range(6):
            object.pencolor(colours[int(flake_length%3)])
            object.pendown()
            object.forward(flake_length)
            drawSnowFlake(turtle_obj, depth - 1, flake_length/3)
            object.penup()
            object.back(flake_length)
            object.right(angle)


if __name__ == "__main__":
    depth = input("Enter the recursive depth of the snowflake: ")
    # The input is being checked for wrong types or non decimal values
    if depth.isdecimal():
        object = turtle.Turtle()
        object._tracer(0,0)
        drawSnowFlake(object, int(depth), 100)
        turtle.done()
    else:
        # returning the appropriate error message for wrong inputs
        print("Enter value is not appropriate!!")