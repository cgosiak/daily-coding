"""
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""
from typing import List, Dict


class Node(object):

    def __init__(self, val: str):
        self.val: str = val
        self.left_node = None
        self.right_node = None


def generate_binary_tree_from_ordered_traversals(pre_order_traversal: List[str], inorder_traversal: List[str]) -> Node:
    root: Node = Node(pre_order_traversal[0])
    nodes: Dict[str, Node] = {
        root.val: root
    }
    in_order_root_index: int = inorder_traversal.index(root.val)

    # There is some weird stuff here, I would say the solution could be handled recursivley to minimize complexity
    # But it is ultimately weird due to the necessity of using the preorder traversal as well

    return root