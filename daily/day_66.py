"""
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a 
probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""
import random
from collections import defaultdict


def toss_biased() -> int:
    return 1 if random.randint(1, 10) <= 7 else 0


def toss_unbiased() -> int:
    is_heads, is_tails = (toss_biased(), toss_biased())
    if (is_heads and not is_tails) or (is_tails and not is_heads):
        return 1 if is_heads else 0
    return toss_unbiased()


biased_results = defaultdict(int)
for i in range(100):
    biased_results[toss_biased()] += 1

print("Biased:", biased_results)

unbiased_results = defaultdict(int)
for i in range(100):
    unbiased_results[toss_unbiased()] += 1

print("Unbiased:", unbiased_results)
