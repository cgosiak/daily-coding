"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""

def pow(a: int, b: int) -> int:
    if b == 0:
        return 1
    temp: int = pow(a, int(b // 2))
    return (temp * temp) if b % 2 == 0 else (temp * temp * a)

print(pow(2, 10))
