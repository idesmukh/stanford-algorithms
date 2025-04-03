# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implements the recursive integer multiplication algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""

import math


def count_digits(number: int) -> int:
    """ Returns the number of decimal digits in an integer.

    Args:
        number: Integer whose digits are to be counted.

    Returns:
        int: Number of digits.
    """

    if number == 0:
        return 1

    # Get absolute value to support negative integers.
    abs_number = abs(number)

    # Calculate base-10 logarithm. 
    log_number = math.log10(abs_number)

    # Round down and add 1 to get digit count.
    # Example:
    #   If log_number = 2.0,
    #   math.floor(2.0) + 1 = 3. 
    return math.floor(log_number) + 1