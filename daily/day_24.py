# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
from typing import List


class Node(object):
    
    def __init__(self, value: int):
        self.value: int = value
        self.locked: bool = False
        self.left_node = None
        self.right_node = None

    def is_locked(self):
        return self.locked

    def can_lock_or_unlock(self):
        checks: List[bool] = []

        if self.left_node is not None:
            checks.append(not self.left_node.is_locked())
            checks.append(self.left_node.can_lock_or_unlock())

        if self.right_node is not None:
            checks.append(not self.right_node.is_locked())
            checks.append(self.right_node.can_lock_or_unlock())

        return False if False in checks else True

    def lock(self):
        if self.can_lock_or_unlock():
            self.locked = True
            return True
        else:
            return False

    def unlock(self):
        if self.can_lock_or_unlock():
            self.locked = False
            return True
        else:
            return False

#                       5
#           3                       7
#      2         4             6         8
root: Node = Node(5)
root.left_node = Node(3)
root.left_node.left_node = Node(2)
root.left_node.right_node = Node(4)
root.right_node = Node(7)
root.right_node.left_node = Node(6)
root.right_node.right_node = Node(8)

root.left_node.right_node.lock()
print("5 unblocked:", root.can_lock_or_unlock())
print("7 unblocked:", root.right_node.can_lock_or_unlock())
print("4 unblocked:", root.left_node.right_node.can_lock_or_unlock())