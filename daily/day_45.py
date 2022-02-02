"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 
implement a function rand7() that returns an integer from 1 to 7 (inclusive)
"""
import random


def rand5() -> int:
    return random.randint(1, 5)

def rand7() -> int:
    # [1, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5, 6, 7]
    possible_vals = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, 0, 0, 0, 0]
    ]
    result = 0
    while result == 0:
        result = possible_vals[rand5() - 1][rand5() - 1]
    return result

for i in range(20):
    print(rand7())