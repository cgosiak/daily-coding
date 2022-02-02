"""
Given an array of strictly the characters 'R', 'G', and 'B', 
segregate the values of the array so that all the Rs come first, 
the Gs come second, and the Bs come last. You can only swap elements of the array.

Do tb_indexs in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
 it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
from typing import List
import unittest

def RGB(rgb_list: List[str]) -> List[str]:
    r_index: int = 0
    g_index: int = 0
    b_index: int = len(rgb_list) - 1

    while g_index <= b_index: 
        if rgb_list[g_index] == 'R': 
            rgb_list[r_index], rgb_list[g_index] = rgb_list[g_index], rgb_list[r_index] 
            r_index = r_index + 1
            g_index = g_index + 1
        elif rgb_list[g_index] == 'G': 
            g_index = g_index + 1
        else: 
            rgb_list[g_index], rgb_list[b_index] = rgb_list[b_index], rgb_list[g_index]  
            b_index = b_index - 1
    return rgb_list


class TestRGB(unittest.TestCase):

    def test_1(self):
        self.assertEqual(RGB(['R', 'G', 'B']), ['R', 'G', 'B'])

    def test_2(self):
        self.assertEqual(RGB(['B', 'G', 'R']), ['R', 'G', 'B'])

    def test_3(self):
        self.assertEqual(RGB(['G', 'B', 'R', 'R', 'B', 'R', 'G']), ['R', 'R', 'R', 'G', 'G', 'B', 'B'])


if __name__ == "__main__":
    unittest.main()
