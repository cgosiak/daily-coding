"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""
def smallest_positive_missing_int(input_array) -> int:
    smallest_found = 1
    for num in input_array:
        if num <= smallest_found:
            smallest_found += num
    return smallest_found

print("Smallest Postive Missing Integer:", smallest_positive_missing_int([1, 2, 3, 10]))