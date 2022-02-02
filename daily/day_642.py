"""
A step word is formed by taking a given word, adding a letter, and anagramming the result.
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.
"""
from typing import List

dictionary = [
    "APPLE",
    "APPEAL",
    "APQEAL",
    "DOG"
]

def is_step_word(word1, word2) -> bool:
    if len(word2) == len(word1) + 1:
        unique_letters = set(word1)
        diffs = 0
        for letter in unique_letters:
            if word1.count(letter) != word2.count(letter):
                diffs += 1
                if diffs > 1:
                    return False
        return True
    return False

def step_words(initial_word) -> List[str]:
    found = [x for x in dictionary if is_step_word(initial_word, x)]
    return found

print("Step Words for (APPLE):", step_words("APPLE"))