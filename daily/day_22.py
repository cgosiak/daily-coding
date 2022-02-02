# Given a dictionary of words and a string made up of those words 
# (no spaces), return the original sentence in a list. If there 
# is more than one possible reconstruction, return any of them. 
# If there is no possible reconstruction, then return null.

# For example, given the set of words 
# 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
# you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 
# 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond"
# , return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
from typing import List, Set


def string_parser(word_list: List[str] or Set[str], input_str: str) -> List[str] or None:
    if type(word_list) == list:
        word_list = set(word_list)

    reconstruction: List[str] = []

    built_word: str = ''
    for char in input_str:
        built_word += char
        if built_word in word_list:
            reconstruction.append(built_word)
            built_word = ''

    return reconstruction if reconstruction else None


print(string_parser(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox'))
print(string_parser(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond'))
print(string_parser(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'radminibed'))