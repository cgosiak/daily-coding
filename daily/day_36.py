"""
Given the root to a binary search tree, find the second largest node in the tree.
"""

class Node(object):

    def __init__(self, value: str):
        self.value = value
        self.left_node = None
        self.right_node = None

    def get_children(self, is_parent: bool = True):
        children = []
        if not is_parent:
            children.append(self.value)
        if self.left_node:
            children.extend(self.left_node.get_children(False))
        if self.right_node:
            children.extend(self.right_node.get_children(False))
        return children

root = Node("A")

root.left_node = Node("B")
root.left_node.left_node = Node("E")
root.left_node.left_node.right_node = Node("F")

root.right_node = Node("C")

left_children = root.left_node.get_children()
right_chilren = root.right_node.get_children()

if len(left_children) > len(right_chilren):
    print("Left Child has more nodes")
elif len(left_children) < len(right_chilren):
    print("Right Child has more nodes")
else:
    print("Equal Nodes")
    