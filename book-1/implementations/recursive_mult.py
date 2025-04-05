# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement the recursive integer multiplication algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""

import math


def count_digits(number: int) -> int:
    """Return the number of decimal digits in an integer.

    Args:
        number: Integer whose digits are to be counted.

    Returns:
        int: Number of digits.
    """

    if number == 0:
        return 1

    # Convert to absolute value to support negative integers.
    abs_number = abs(number)

    # Calculate base-10 logarithm. 
    log_number = math.log10(abs_number)

    # Round down and add 1 to get digit count.
    # Example:
    #   If log_number = 2.0,
    #   math.floor(2.0) + 1 = 3. 
    return math.floor(log_number) + 1


def rec_int_mult(x: int, y: int) -> int:
    """Multiply two n-digit positive integers recursively.

    Implement a divide-and-conquer approach to multiplication.
    Assume n is a power of 2 i.e. integers have even digits.

    Args:
        x: First integer.
        y: Second integer.

    Returns:
        int: Product of x and y.
    """

    if x < 0 or y < 0:
        raise ValueError("Inputs must be positive integers")

    if x < 10 and y < 10:
        return x * y

    digits_x = count_digits(x)
    digits_y = count_digits(y)

    # Assign number of digits value to n.
    n = max(digits_x, digits_y)
    half_n = n // 2

    # Split x into higher order (a) and lower order (b) parts.
    a = x // (10**half_n)
    b = x % (10** half_n)

    # Split y into higher order (c) and lower order (d) parts.
    c = y // (10**half_n)
    d = y % (10**half_n)

    ac = rec_int_mult(a, c)
    ad = rec_int_mult(a, d)
    bc = rec_int_mult(b, c)
    bd = rec_int_mult(b, d)

    # Combine results: ac * 10^n + (ad + bc) * 10^(n / 2) + bd.
    term_1 = 10**n * ac
    term_2 = 10**(n // 2) * (ad + bc)
    term_3 = bd

    return term_1 + term_2 + term_3


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert rec_int_mult(0, 5) == 0
    assert rec_int_mult(99, 99) == 9801
    print("All tests passed!")