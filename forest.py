"""
forest.py
This class has the capability to draw a forest at night and a harvested day.
The number of trees in the forest is taken as input from the user and asked if a house to be present at night or not. The
night is also decorated with a star. Once it is done, the total forest is harvested and the available lumber is used to
draw a house on the day. A sun is also present to indicate the day.
@version: 1.0

@author: Santosh Kumar Nunna (sn7916@rit.edu)
@author: Mouna Reddy Kallu (mk9014@rit.edu)
"""
import turtle
import random
import math

class Forest:
    def __init__(self, turtle_obj, no_of_trees, house_present):
        """
        The constructor which initializes all the objects
        :param turtle_obj: This is the turtle object
        :param no_of_trees: Total number of trees to be drawn
        :param house_present: Whether the house is present or not
        """
        self.pointer = turtle_obj
        self.tree_count = no_of_trees
        self.house_present = house_present
        self.leaf_length = 30
        self.sum = 0
        self.pointer.up()
        self.pointer.setheading(0)
        turtle.title('Forest')

    def night_trees(self):
        """
        Draws 3 types of trees in the night time
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: sum of the lengths of the lumber available from the trees and house(if present)
        """
        if self.tree_count > 3:
            tree_position = random.randint(1, self.tree_count)
        else:
            tree_position = self.tree_count - 1
        for index in range(0,self.tree_count):
            tree_length = random.randint(50, 201)
            self.sum = self.sum + tree_length;

            if(index == tree_position):
                if str(self.house_present).lower() != 'n':
                    self.house(341.4, False)

            self.pointer.left(90)
            self.pointer.down()
            self.pointer.forward(tree_length)
            self.pointer.up()
            self.pointer.right(90)

            # Type 1 - Maple Tree
            if (tree_length < 100):
                self.pointer.down()
                self.pointer.circle(self.leaf_length)
                self.pointer.up()

            # Type 2 - Hexa Tree
            elif (tree_length > 100 and tree_length < 150):
                self.pointer.forward(self.leaf_length / 2)
                self.pointer.down()
                for _ in range(0, 6):
                    self.pointer.left(360 / 6)
                    self.pointer.forward(self.leaf_length)
                self.pointer.up()
                self.pointer.back(self.leaf_length / 2)


            # Type 3 - Pine Tree
            else:
                self.pointer.forward(self.leaf_length)
                self.pointer.down()
                for _ in range(0, 3):
                    self.pointer.left(120)
                    self.pointer.forward(2*self.leaf_length)
                self.pointer.up()
                self.pointer.back(self.leaf_length)

            self.pointer.right(90)
            self.pointer.forward(tree_length)
            if index != self.tree_count-1 :
                self.pointer.down()
            self.pointer.left(90)
            self.pointer.forward(100)
            self.pointer.up()

        if self.house_present != "n":
            self.sum += 341.4
        return self.sum;

    def house(self, total_lumber, is_morning):
        """
        Draws a house in the morning or night according the lumber available
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :param total_lumber: Amount of lumber available
        :param is_morning: Whether we are drawing in morning or not
        :return: None
        """
        wood_length = total_lumber/(3.414)
        print("We will build a house with walls " + str(wood_length) + " tall.")
        wood_length = wood_length/2
        if is_morning:
            self.pointer.reset()
        self.pointer.down()
        self.pointer.left(90)
        self.pointer.forward(wood_length)
        self.pointer.right(45)
        self.pointer.forward(wood_length / math.sqrt(2))
        self.pointer.right(90)
        self.pointer.forward(wood_length / math.sqrt(2))
        self.pointer.right(45)
        self.pointer.forward(wood_length)
        self.pointer.left(90)
        if is_morning:
            self.pointer.up()
        self.pointer.forward(100)
        self.pointer.up()
        if is_morning:
            self.draw_sun(wood_length)

    def draw_sun(self, height):
        """
        Draws the sun in the morning
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :param height: Height above which the sun has to be drawn
        :return: None
        """
        self.pointer.forward(50)
        self.pointer.left(90)
        self.pointer.forward(height + 100)
        self.pointer.down()
        self.pointer.circle(self.leaf_length)

    def draw_star(self):
        """
        Draws the star in the night
        :pre: (relative) pos (0,0), heading (east), up
        :post: (relative) pos (0,0), heading (east), up
        :return: None
        """
        self.pointer.left(90)
        self.pointer.forward(250)
        for _ in range(0, 6):
            self.pointer.left(360 / 6)
            self.pointer.down()
            self.pointer.back(self.leaf_length)
            self.pointer.forward(self.leaf_length)
        self.pointer.up()


def main():
    """
    The main function where the process is performed like taking inputs from the user and calling the necessary
    funtions to draw the night and the day of a forest using turtle.
    :return: None
    """
    numberOfTrees = int(input("Enter number of trees: "))
    house_present = input("Is there a house in the forest (y/n): ")
    pointer = turtle.Turtle()
    pointer.hideturtle()
    forest = Forest(pointer, numberOfTrees, house_present)
    total_lumber = forest.night_trees()
    forest.draw_star()
    to_morning = input("Night is Done. Press Enter for Day!")
    print("We have " + str(total_lumber) + " units of lumber for building.")
    if len(to_morning) >= 0:
        pointer.reset()
        forest = Forest(pointer, numberOfTrees, house_present)
        forest.house(total_lumber, True)
    to_close = input("Day is done, house is built, Press enter to quit.")
    if len(to_close) >= 0:
        turtle.Screen().bye()


if __name__ == '__main__':
    main()

