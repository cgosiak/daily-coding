"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""
from typing import List


def max_sum_from_contiguous_subarray(input_list: List[int]) -> int:
    max_sum: int = 0

    temp_sum: int = 0
    for element in input_list:
        temp_sum += element
        if temp_sum < 0:
            temp_sum = 0
        if temp_sum > max_sum:
            max_sum = temp_sum

    return max_sum


print(max_sum_from_contiguous_subarray([34, -50, 42, 14, -5, 86]))
print(max_sum_from_contiguous_subarray([-5, -1, -8, -9]))