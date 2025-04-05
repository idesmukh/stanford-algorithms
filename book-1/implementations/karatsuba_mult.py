# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement the karatsuba multiplication algorithm.

Uses three recursive calls, instead of four recursive calls as per standard
recursive integer multiplication.

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


def karatsuba(x: int, y: int) -> int:
    """Multiply two n-digit positive integers recursively.

    Implement a divide-and-conquer approach to integer multiplication.
    Assume n is a power of 2 i.e. integers have even number of digits.
    Total number of recursive calls is three.

    Args:
        x: First integer.
        y: Second integer.

    Returns:
        int: The product of x and y.
    """

    if x < 0 or y < 0:
        raise ValueError("Inputs must be positive integers")

    if x < 10 and y < 10:
        return x * y

    digits_x = count_digits(x)
    digits_y = count_digits(y)

    n = max(digits_x, digits_y)
    half_n = n // 2

    # Split x into higher order (a) and lower order (b) parts.
    a = x // (10**half_n)
    b = x % (10**half_n)

    # Split y into higher order (c) and lower order (d) parts.
    c = y // (10**half_n)
    d = y % (10**half_n)

    # Compute p and q using grade-school addition.
    p = a + b
    q = c + d

    # Recursively compute subproducts.
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)

    # Compute a.d + b.c using grade-school addition.
    # (a + b).(c + d) - a.c - b.d = a.d + b.c.
    # We already have (a + b).(c + d), a.c and b.d, so we calculate a.d + b.c.
    adbc = pq - ac - bd

    # Combine results: ac * 10^n + (ad + bc) * 10^(n/2) + bd.
    term_1 = 10**n * ac
    term_2 = 10**(n // 2) * (adbc)
    term_3 = bd

    # Perform basic addition to compute x.y.
    return term_1 + term_2 + term_3


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert karatsuba(0, 5) == 0
    assert karatsuba(99, 99) == 9801
    print("All tests passed!")