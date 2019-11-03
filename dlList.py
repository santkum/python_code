"""
dlList.py
This file has the implementation of the functionality associated with double linked list which imports over the node
functionality.

@author: Santosh Kumar Nunna (sn7916@rit.edu)
@author: Mouna Reddy Kallu (mk9014@rit.edu)
"""
from dlNode import Node


class LinkedNode:
    def __init__(self):
        self.current = self.start = None

    def push(self, value, last=False):
        """
        This method adds the new entry to the clockwise direction and the last entry is pointed to the first element to
        achieve circular linked list.
        :param value: value to be added in the list
        :param last: Boolean value to indicate the end of entries. Default is False, if True, the last entry's next is
        pointed to the first entry.
        :return: None
        """
        new_node = Node(value)
        if self.current is None:
            self.start = self.current = new_node
        else:
            self.current.next = new_node
            new_node.prev = self.current
            self.current = new_node
        if last:
            self.current.next = self.start
            self.start.prev = self.current
            self.current = self.current.next

    def pop(self, clockwise=True):
        """
        The pop method removes the current value and makes the next/previous of current value as current based on the
        clockwise value.
        :param clockwise: True if the traversal happens in the clockwise direction and next element is in the clockwise
        direction else previous element is pointed as current value.
        :return: None
        """
        if self.current != self.current.next:
            print(self.current.value + " is stuck holding the potato!")
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            if clockwise:
                self.current = self.current.next
            else:
                self.current = self.current.prev

    def print_all(self):
        """
        This function returns the list of the names in the linked list starting from the current value.
        :return: List of names
        """
        current1 = self.current
        li = list()
        while True:
            li.append(current1.value)
            current1 = current1.next
            if current1 == self.current:
                return li

    def traverse(self, steps):
        """
        The traverse function moves the current value based on the steps input. If steps is positive it moves in clock
        wise direction else anti clockwise. If it is zero the current values doesn't change. When the traversal is
        complete the current value is popped.
        :param steps: number of steps to be traversed
        :return: None
        """
        print("The music starts (" + str(steps) + "): ", end='')
        if steps > 0:
            for x in range(steps):
                print(self.current.value, end='->')
                self.current = self.current.next
            self.pop()
        elif steps < 0:
            for x in range(abs(steps)):
                print(self.current.value, end='->')
                self.current = self.current.prev
            self.pop(False)
        else:
            self.current = self.current
            self.pop()
