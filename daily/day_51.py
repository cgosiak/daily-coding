"""
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, 
write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
from typing import List
import random

def get_shuffled_deck() -> List[int]:
    deck: List[int] = [x for x in range(52)]

    for i in range(len(deck)):
        swap_position: int = random.randint(0, len(deck) - 1)
        deck[i], deck[swap_position] = deck[swap_position], deck[i]

    return deck

print(get_shuffled_deck())