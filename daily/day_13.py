from typing import Set

def get_longest_substring_of_k_distinct_chars(input_str: str, k: int) -> str:
    longest_str: str = ''
    potential_str: str = ''
    unique_chars: Set[str] = set()
    input_str_length: int = len(input_str)

    for i in range(input_str_length):
        unique_chars = set([input_str[i]])
        potential_str = ''
        for j in range(i, input_str_length):
            potential_addition: str = input_str[j]
            if potential_addition in unique_chars:
                potential_str += potential_addition
            else:
                if len(unique_chars) == k:
                    if len(potential_str) > len(longest_str):
                        longest_str = potential_str
                else:
                    unique_chars.add(potential_addition)
                    potential_str += potential_addition

    return longest_str if len(longest_str) > 0 else input_str


print(get_longest_substring_of_k_distinct_chars('abcba', 2))
print(get_longest_substring_of_k_distinct_chars('abcba', 3))