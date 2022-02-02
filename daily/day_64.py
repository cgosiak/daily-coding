"""
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.
"""

def get_knights_tours(n: int) -> int:
    board = [
        [-1 for i in range(n)] for k in range(n)
    ]

    # Always start at top left

    return "\n".join([" ".join([str(x) for x in row]) for row in board])

print(get_knights_tours(8))