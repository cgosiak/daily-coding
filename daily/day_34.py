"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters 
as possible anywhere in the word. If there is more than one palindrome of minimum length 
that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", 
since we can add three letters to it (which is the smallest amount to make a palindrome). 
There are seven other palindromes that can be made from "race" by adding three letters, 
but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""
import unittest


def is_palindrome(word: str) -> bool:
    return word == word[::-1]

def find_palindrome(word: str) -> str:
    palindromes = []
    for i in range(len(word), 1, -1):
        sub_word: str = word[:i]
        if is_palindrome(sub_word):
            if sub_word == word:
                return word
            else:
                prefix: str = word.replace(sub_word, "")[::-1]
                return f"{prefix}{word}"
    
    sub_word: str = word[1:]
    return f"{sub_word[::-1]}{word[0]}{sub_word}"

def find_best_palindrome(word: str) -> str:
    return sorted([find_palindrome(word), find_palindrome(word[::-1])])[0]


class TestPalindromes(unittest.TestCase):

    def test_otto(self):
        self.assertEqual(find_best_palindrome("otto"), "otto")

    def test_race(self):
        self.assertEqual(find_best_palindrome("race"), "ecarace")

    def test_google(self):
        self.assertEqual(find_best_palindrome("google"), "elgoogle")
    
    def test_ashs(self):
        self.assertEqual(find_best_palindrome("ashs"), "ashsa")


if __name__ == "__main__":
    unittest.main()