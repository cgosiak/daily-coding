"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(),  which pops off and returns the topmost element of the stack. 
        If there are no elements in the stack, then it should throw an error or return null.
max(),  which returns the maximum value in the stack currently. If there are no 
        elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""
from typing import List


class Stack(object):

    def __init__(self):
        self.values: List[int] = []
        self.max_value: int = None

    def push(self, val: int):
        if not self.values:
            self.values.append(val)
            self.max_value = val
        else:
            if val > self.max_value:
                self.values.append((2 * val) - self.max_value)
                self.max_value = val
            else:
                self.values.append(val)

    def pop(self):
        if not self.values: 
            return None 
        else: 
            removedNode = self.values.pop()
            if removedNode > self.max_value: 
                self.max_value = ( ( 2 * self.max_value ) - removedNode )
                return (removedNode + self.max_value) // 2
            return removedNode

    def max(self):
        return self.max_value


stack: Stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)

print(stack.max())
print(stack.pop())
print(stack.max())