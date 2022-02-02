"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""
from typing import Set, List
import unittest
import math


def super_set(given_set: List[int]) -> List[List[int]]:
    all_sets: List[List[int]] = []
    pow_set_size = int(math.pow(2, len(given_set)))

    for counter in range(pow_set_size):
        values = []
        for j in range(len(given_set)):
            if (counter & (1 << j)) > 0:
                values.append(given_set[j])
        all_sets.append(values)

    return all_sets


vals = super_set(["A", "B", "C"])
print(vals)
