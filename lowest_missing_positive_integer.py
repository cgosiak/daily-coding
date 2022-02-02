from typing import List, Set

# Requirements
# Time -> O(n)
# Space -> O(n)
def get_lowest_missing_positive_integer(nums: List[int]) -> int:
    if not nums:
        return 1
    nums_as_set: Set[int] = set(nums)
    max_int: int = max(nums)

    for i in range(1, max_int + 2):
        if i not in nums_as_set:
            return i

def quick_test(arr: List[int], expected_answer: int):
    derived_ans: int = get_lowest_missing_positive_integer(arr)
    print(arr, "derived", derived_ans, derived_ans == expected_answer)

# Test Cases
quick_test([], 1)
quick_test([1, 2, 0], 3)
quick_test([3, 4, -1, 1], 2)
quick_test([2, 4, -1, 1], 3)