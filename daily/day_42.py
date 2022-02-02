"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S 
that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
import unittest
import math
from typing import List


def get_super_set(input_list: List[int]) -> List[List[int]]:
    total_set_size: int = int(math.pow(2, len(input_list)))
    sets: List[List[int]] = []

    for counter in range(total_set_size):
        current_set: List[int] = []
        for j in range(len(input_list)):
            if (counter & (1 << j)) > 0:
                current_set.append(input_list[j])
        sets.append(current_set)

    return sets


def get_sum_subset(given_numbers: List[int], desired_sum: int) -> List[int] or None:
    all_sets: List[List[int]] = get_super_set(given_numbers)

    for optional_set in all_sets:
        if sum(optional_set) == desired_sum:
            return optional_set

    return None


class TestSubsetAddition(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_sum_subset([1, 2], 4), None)

    def test_2(self):
        self.assertEqual(sorted(get_sum_subset([12, 1, 61, 5, 9, 2], 24)), sorted([12, 1, 9, 2]))


unittest.main()
