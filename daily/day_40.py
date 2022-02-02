"""
Given an array of integers where every integer occurs three times except for one integer, 
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
from typing import List, DefaultDict
from collections import defaultdict
import unittest


def find_non_duplicated_integer(given_list: List[int]) -> int:
    options: DefaultDict = defaultdict(int)

    for entry in given_list:
        options[entry] += 1
        if options[entry] == 3:
            del options[entry]

    return list(options.keys())[0]


class TestNonDuplicatedInteger(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_non_duplicated_integer([6, 1, 3, 3, 3, 6, 6]), 1)

    def test_2(self):
        self.assertEqual(find_non_duplicated_integer([13, 19, 13, 13]), 19)

unittest.main()
