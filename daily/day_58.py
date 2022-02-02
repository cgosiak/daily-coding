"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. 
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""
from typing import List
import unittest


def binary_search(input_list: List[int], item_to_find: int, index_shift: int = 0) -> int or None:
    # Look for 6
    # [2, 4, 6, 8, 10]
    # -> [2, 4] and [6, 8, 10]
    # --> [6] and [8, 10]
    # ---> return index

    # [10, 2, 4, 6, 8]
    # -> [10, 2] and [4, 6, 8]
    # --> [4] and [6, 8]
    # ---> [6] and [8]
    # ----> return index
    
    # [8, 10, 2, 4, 6]
    # -> [8, 10] and [2, 4, 6]
    # --> [2] and [4, 6]
    # ---> [4] and [6]
    # ----> return index

    # [6, 8, 10, 2, 4]
    # -> [6, 8] and [10, 2, 4]
    # --> [6] and [8]
    # ---> return index

    # [4, 6, 8, 10, 2]
    # -> [4, 6] and [8, 10, 2]
    # --> [4] and [6]
    # ---> return index
    if len(input_list) == 0:
        return None
    elif len(input_list) == 1:
        return index_shift if input_list[0] == item_to_find else None
    
    pivot: int = int(len(input_list) // 2)
    left_side: List[int] = input_list[:pivot]
    right_side: List[int] = input_list[pivot:]

    if left_side[0] < left_side[len(left_side) - 1]:
        # left side is sorted
        if left_side[0] <= item_to_find <= left_side[len(left_side) - 1]:
            return binary_search(left_side, item_to_find, index_shift)
        else:
            return binary_search(right_side, item_to_find, index_shift + len(left_side))
    else:
        # right side is sorted
        if right_side[0] <= item_to_find <= right_side[len(right_side) - 1]:
            return binary_search(right_side, item_to_find, index_shift + len(left_side))
        else:
            return binary_search(left_side, item_to_find, index_shift)



def get_index(input_list: List[int], item: int) -> int or None:
    return binary_search(input_list, item)


class TestGetIndex(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_index([13, 18, 25, 2, 8, 10], 8), 4)

    def test_2(self):
        self.assertEqual(get_index([13, 18, 25, 2, 8, 10], 1), None)


unittest.main()
