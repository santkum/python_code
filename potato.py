"""
potato.py
This file has the implementation of the potato contest.

@author: Santosh Kumar Nunna (sn7916@rit.edu)
@author: Mouna Reddy Kallu (mk9014@rit.edu)
"""
from dlList import LinkedNode
import sys
import random


class Potato:
    def __init__(self):
        self.file = sys.argv[1]
        self.seed = int(sys.argv[2])
        self.ln = LinkedNode()

    def show_off(self):
        """
        This function shows the initial welcome text and the contestants of the game.
        :return: None
        """
        print("Welcome to the Hot Potato Game!\n")
        print("Reading from: " + self.file)
        with open(self.file, 'r') as file_ptr:
            name_list = file_ptr.readlines()
            for index, name in enumerate(name_list):
                if index == len(name_list)-1:
                    self.ln.push(name.strip(), True)
                else:
                    self.ln.push(name.strip())
        print("Using random number generator seed: " + str(self.seed))
        print("Ready to play Hot Potato. Contestants are:\n")
        name_list = self.ln.print_all()
        for x in name_list:
            print(x, end=', ')
        print()

    def start_game(self):
        """
        This function starts the game and prints the winner.
        :return: None
        """
        counter = len(self.ln.print_all())
        random.seed(self.seed)
        while counter != 1:
            self.ln.traverse(random.randint(-counter*2, counter*2))
            counter = len(self.ln.print_all())
        li = self.ln.print_all()
        print( li[0] + " is the winner!!")

if __name__ == "__main__":
    p = Potato()
    p.show_off()
    p.start_game()
