import sys


class binarytree(object):
    """Implements a binary tree"""

    def __init__(self, value, left=-1, right=-1):
        self.value = value
        self.left = left
        self.right = right
        self.num_left = 0
        self.num_right = 0

    def insert(self, value, left=-1, right=-1):
        if self.left == -1:
            new_tree = binarytree(value, left, right)
            self.left = new_tree
            self.num_left += 1
            return 0

        if self.right == -1:
            new_tree = binarytree(value, left, right)
            self.right = new_tree
            self.num_right += 1
            return 0

        if self.num_left >= self.num_right:
            self.left.insert(value, left, right)
            self.num_left += 1
            return 0

        if self.num_right > self.numleft:
            self.right.insert(value, left, right)
            self.num_right += 1
            return 0

    def inorder_traversal(self):
        if self.left == -1:
            sys.stdout.write(self.value + " ")
