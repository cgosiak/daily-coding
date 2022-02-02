# You are given an array of non-negative integers that represents 
# a two-dimensional elevation map where each element is unit-width 
# wall and the integer is the height. Suppose it will rain and all 
# spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
# 2 in the second, and 3 in the fourth index 
# (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
from typing import List
import unittest


def calculate_bucket_area(input_array: List[int]) -> int:
    area: int = 0
    left_wall: int or None = None
    low_pt: int or None = None

    potential_area: int = 0
    for pt in input_array:
        if left_wall is None or pt >= left_wall:
            area += potential_area
            potential_area = 0
            left_wall = pt
        else:
            if low_pt is None or pt < low_pt:
                low_pt = pt
            potential_area += (left_wall - pt)
            if pt > low_pt:
                area += (pt - low_pt)
                potential_area -= (pt - low_pt)

    return area


class TestBucketAlgorithm(unittest.TestCase):

    def test_1(self):
        self.assertEquals(calculate_bucket_area([2, 1, 2]), 1)

    def test_2(self):
        self.assertEquals(calculate_bucket_area([3, 0, 1, 3, 0, 5]), 8)

    def test_3(self):
        self.assertEquals(calculate_bucket_area([0, 1, 3, 0, 5]), 3)

    def test_4(self):
        self.assertEquals(calculate_bucket_area([0, 1, 3]), 0)

    def test_5(self):
        self.assertEquals(calculate_bucket_area([2, 1, 2]), 1)

    def test_6(self):
        self.assertEquals(calculate_bucket_area([3, 1, 2]), 1)

    def test_7(self):
        self.assertEquals(calculate_bucket_area([2, 1, 3]), 1)

if __name__ == "__main__":
    unittest.main()