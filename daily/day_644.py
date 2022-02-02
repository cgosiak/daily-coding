# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:

    def __init__(self, value: int):
        self.value: int = value
        self.left: Node = None
        self.right: Node = None

    def is_unival(self) -> bool:
        if self.left:
            if self.left.value != self.value or not self.left.is_unival():
                return False
        if self.right:
            if self.right.value != self.value or not self.right.is_unival():
                return False
        return True

    def unival_subtree_count(self) -> int:
        unival_count: int = 0
        if self.is_unival():
            unival_count += 1
        if self.left:
            unival_count += self.left.unival_subtree_count()
        if self.right:
            unival_count += self.right.unival_subtree_count()
        return unival_count

# Setup Tree
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

print("Unival Count:", root.unival_subtree_count())