"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. 
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

def find_pivot(input_array) -> int:
    pointer = len(input_array) // 2
    left_arr, right_arr = (input_array[:pointer], input_array[pointer:])
    if input_array[pointer] > input_array[pointer - 1] and input_array[pointer] < input_array[pointer + 1]:
        return find_pivot(left_arr) or find_pivot(right_arr)
    return min([input_array[pointer-1], input_array[pointer], input_array[pointer+1]])

print("Pivot Array:", find_pivot([5, 7, 10, 3, 4]))