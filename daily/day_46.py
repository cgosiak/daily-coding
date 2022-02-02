"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""
from typing import List

def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def longest_palindrome_in_string(input_string: str) -> str or None:
    longest_palindrome: str = ""

    for i in range(len(input_string)):
        substring: str = input_string[i]
        for k in range(i + 1, len(input_string)):
            substring += input_string[k]
            if is_palindrome(substring) and len(substring) > len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome if len(longest_palindrome) > 1 else None


print(longest_palindrome_in_string("bananas"))
