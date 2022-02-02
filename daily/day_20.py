# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
from typing import List


def find_intersection(path_1: List[int], path_2: List[int]) -> int:
    return set(path_1).intersection(set(path_2)).pop()

print(find_intersection([3, 7, 8, 10], [99, 1, 8, 10]))