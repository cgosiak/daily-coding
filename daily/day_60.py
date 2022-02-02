"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can 
split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it 
up into two subsets that add up to the same sum.
"""
from typing import List
import unittest
import math


def set_sum_exists(input_list: List[int], required_sum: int) -> bool:
    total_subsets: int = int(math.pow(2, len(input_list)))

    for counter in range(total_subsets):
        current_set: List[int] = []
        for j in range(len(input_list)):
            if (counter & (1 << j)) > 0:
                current_set.append(input_list[j])
        if sum(current_set) == required_sum:
            return True

    return False


def creates_multiset_same_sum(input_list: List[int]) -> bool:
    # [1, 2, 3]
    # --> [1, 2] and [3]

    # [2, 4, 6]
    # --> [2, 4] and [6]

    # of the total sum, half of that value will exist in an array
    # odd total_sums can not be found in an array of integers
    total_sum: int = sum(input_list)

    if total_sum % 2 == 0:
        subset_sum: int = total_sum / 2
        # we need to find an array which exists that adds up to the subset sum
        return set_sum_exists(input_list, subset_sum)
    return False


class TestMultisetSummations(unittest.TestCase):

    def test_1(self):
        self.assertTrue(creates_multiset_same_sum([15, 5, 20, 10, 35, 15, 10]))
    
    def test_2(self):
        self.assertFalse(creates_multiset_same_sum([15, 5, 20, 10, 35]))


unittest.main()
