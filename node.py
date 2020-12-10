"""
Author: James Lawson, Harry Pinkerton, James Lawson
File: node.py
Project: 4
"""

class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next = None):
        self.data = data
        self.next = next
