"""
We can determine how "out of order" an array A is by counting the number of inversions it has. 
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller 
element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three 
inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: 
every distinct pair forms an inversion.
"""
from typing import List
import unittest


def count_inversions(given_list: List[int]) -> int:
    total_inversions: int = 0
    temp_inversions: int = 0
    for i in range(len(given_list)):
        element_a: int = given_list[i]
        previous_element: int = given_list[i - 1] if i > 0 else None
        if previous_element is not None and previous_element > element_a:
            temp_inversions -= 1
            total_inversions += temp_inversions
            continue
        else:
            temp_inversions = 0
        for k in range(i + 1, len(given_list)):
            element_b: int = given_list[k]
            if element_a > element_b:
                temp_inversions += 1
        total_inversions += temp_inversions
    return total_inversions


class TestInversionCounting(unittest.TestCase):

    def test_1(self):
        self.assertEqual(count_inversions([]), 0)

    def test_2(self):
        self.assertEqual(count_inversions([2, 4, 1, 3, 5]), 3)

    def test_3(self):
        self.assertEqual(count_inversions([5, 4, 3, 2, 1]), 10)

    def test_4(self):
        self.assertEqual(count_inversions([3, 2, 1]), 3)


unittest.main()
