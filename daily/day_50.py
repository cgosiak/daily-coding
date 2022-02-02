"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class Node(object):

    def __init__(self, val):
        self.val = val
        self.is_operator: bool = self.val in ["+", "−", "*", "/"]
        self.left_node = None
        self.right_node = None

    def get_arithmetic_val(self) -> int:
        if not self.is_operator:
            return int(self.val)
        else:
            if self.val == '+':
                return self.left_node.get_arithmetic_val() + self.right_node.get_arithmetic_val()
            elif self.val == '-':
                return self.left_node.get_arithmetic_val() - self.right_node.get_arithmetic_val()
            elif self.val == '*':
                return self.left_node.get_arithmetic_val() * self.right_node.get_arithmetic_val()
            elif self.val == '/':
                return self.left_node.get_arithmetic_val() / self.right_node.get_arithmetic_val()


root = Node("*")
root.left_node = Node("+")
root.left_node.left_node = Node("3")
root.left_node.right_node = Node("2")

root.right_node = Node("+")
root.right_node.left_node = Node("4")
root.right_node.right_node = Node("5")

print(root.get_arithmetic_val())
