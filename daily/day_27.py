# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.
from typing import List


def has_properly_formatted_brackets(input_str: str) -> bool:
    char_list: List[str] = []
    matching_brackets = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for char in input_str:
        if char in matching_brackets.keys():
            char_list.append(char)
        else:
            if char != matching_brackets[char_list.pop()]:
                return False
    return True

print(has_properly_formatted_brackets("([])[]({})"))
print(has_properly_formatted_brackets("([)]"))