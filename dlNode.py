"""
dlNode.py
This file has the implementation of the node functionality.

@author: Santosh Kumar Nunna (sn7916@rit.edu)
@author: Mouna Reddy Kallu (mk9014@rit.edu)
"""
__slots__ = "value", "next", "previous"

class Node:
    def __init__(self, value, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.value = value