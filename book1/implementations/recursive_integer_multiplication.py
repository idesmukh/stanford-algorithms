"""Implements the recursive integer multiplication (RecIntMult) algorithm from Algorithms Illuminated.

This module provides an efficient method for multiplying large integers using recursion.
"""

import math


def count_digits(number: int) -> int:
    """Return the number of decimal digits in an integer.

    Args:
        number: An integer whose digits are to be counted

    Returns:
        int: The number of digits (e.g., 1 for 0, 3 for 123).
    """

    if number == 0:
        return 1

    return math.floor(math.log10(abs(number))) + 1


def rec_int_mult(x: int, y: int) -> int:
    """Multiply two positive even integers recursively using the RecIntMult algorithm.

    This implements a divide-and-conquer approach to integer multiplication.
    Assumes inputs are positive even integers; behavior is undefined for negative numbers.

    Args:
        x: First positive even integer
        y: Second positive even integer

    Returns:
        int: The product of x and y.
    """

    if x < 10 and y < 10:
        return x * y

    digits_x = count_digits(x)
    digits_y = count_digits(y)

    n = max(digits_x, digits_y)

    # Split x into higher order (a) and lower order (b) parts based on half its digits
    a = x // (10**(digits_x//2))
    b = x % (10**(digits_x//2))

    # Split y into higher order (c) and lower order (d) parts
    c = y // (10**(digits_y//2))
    d = y % (10**(digits_y//2))

    # Recursively compute subproducts
    ac = rec_int_mult(a, c)
    ad = rec_int_mult(a, d)
    bc = rec_int_mult(b, c)
    bd = rec_int_mult(b, d)

    # Combine results: ac * 10^n + (ad + bc) * 10^(n/2) + bd
    term_1 = 10**n * ac
    term_2 = 10**(n // 2) * (ad + bc)
    term_3 = bd

    return term_1 + term_2 + term_3


if __name__ == "__main__":
    # Verify the algorithm with a simple test case
    assert rec_int_mult(24, 36) == 24 * 36
    print("All tests passed!")