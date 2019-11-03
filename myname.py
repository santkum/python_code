"""
Version: 1.1
Revision: 1
The given class has the functionality to print different letters using the turtle module.

@author: Santosh Kumar Nunna (sn7916@rit.edu)
"""
import turtle
pen = turtle.Turtle()


class Name:
    def __init__(self):
        """
        This is the init function where the window size is set and the turtle pointer head is hidden.
        The speed of the cursor is 0.
        The middle point being (0,0) is where we start to move the turtle
        """
        pen.up()
        pen.setheading(0)
        pen.hideturtle()
        turtle.title("My name")
        pen.speed(0)
        pen.right(90)
        pen.forward(40)
        pen.left(90)

    def draw_s(self):
        """
        This function has the capability to draw the letter 'S'
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.down()
        pen.forward(40)
        pen.left(90)
        pen.forward(20)
        pen.left(90)
        pen.forward(40)
        pen.right(90)
        pen.forward(20)
        pen.right(90)
        pen.forward(40)
        pen.up()
        pen.back(40)
        pen.right(90)
        pen.forward(40)
        pen.left(90)
        pen.forward(50)

    def draw_a(self):
        """
        This function has the capability to draw the letter 'A'
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.down()
        pen.left(90)
        pen.forward(40)
        pen.right(90)
        pen.forward(40)
        pen.right(90)
        pen.forward(40)
        pen.up()
        pen.back(20)
        pen.right(90)
        pen.down()
        pen.forward(40)
        pen.up()
        pen.left(90)
        pen.forward(20)
        pen.left(90)
        pen.forward(50)

    def draw_n(self):
        """
        This function has the capability to draw the letter 'N'
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.down()
        pen.left(90)
        pen.forward(40)
        pen.right(135)
        pen.forward(1.414*40)
        pen.left(135)
        pen.forward(40)
        pen.up()
        pen.back(40)
        pen.right(90)
        pen.back(40)
        pen.forward(50)

    def draw_t(self):
        """
        This function has the capability to draw the letter 'T'
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.forward(20)
        pen.left(90)
        pen.down()
        pen.forward(40)
        pen.right(90)
        pen.up()
        pen.forward(20)
        pen.down()
        pen.back(40)
        pen.up()
        pen.right(90)
        pen.forward(40)
        pen.left(90)
        pen.forward(50)

    def draw_o(self):
        """
        This function has the capability to draw the letter 'O'
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.down()
        pen.forward(40)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
        pen.forward(40)
        pen.left(90)
        pen.up()
        pen.forward(50)

    def draw_h(self):
        """
        This function has the capability to draw the letter 'H'
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.forward(40)
        pen.left(90)
        pen.down()
        pen.forward(40)
        pen.up()
        pen.back(20)
        pen.left(90)
        pen.down()
        pen.forward(40)
        pen.right(90)
        pen.up()
        pen.forward(20)
        pen.down()
        pen.back(40)
        pen.right(90)
        pen.up()
        pen.forward(50)

    def give_space(self):
        """
        This function has the capability to provide a spacing between the letters
        pre: pos (0,0), heading (east)
        post: pos (0,0), heading (east)
        :return: None
        """
        pen.forward(20)


if __name__ == "__main__":
    name = Name()
    name.draw_s()
    name.draw_a()
    name.draw_n()
    name.draw_t()
    name.draw_o()
    name.draw_s()
    name.draw_h()
    name.give_space()
    name.draw_n()
    turtle.done()
