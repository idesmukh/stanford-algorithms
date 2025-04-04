# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement merge sort algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""


def merge_sort(a: list) -> list:
    """Sort a list from smallest to largest integer using merge sort algorithm.

    Args:
        a: List of integers.

    Returns:
        list: New list of integers sorted from smallest to largest.
    """

    # Define base case.
    # If list length is 0 or 1, it is already sorted so return it as it is.
    if len(a) <= 1:
        return a

    # Define recursive case.
    # Divide list 'a' into two halves.
    middle_index = len(a) // 2
    a_left = a[:middle_index]
    a_right = a[middle_index:]

    sorted_left = merge_sort(a_left)
    sorted_right = merge_sort(a_right)

    return merge(sorted_left, sorted_right)


def merge(c: list, d: list) -> list:
    """Merge two sorted lists.

    Args:
        c: First sorted list of integers.
        d: Second sorted list of integers.

    Returns:
        list: New list containing 'c' and 'd' sorted from smallest to largest.
    """

    # Initialize output list.
    b = []

    # Initialise pointers for 'c' and 'd'.
    i = 0
    j = 0

    # Fill output list with sorted elements from 'c' and 'd'.
    while i < len(c) and j < len(d):
        if c[i] < d[j]:
            b.append(c[i])
            i += 1
        else: # d[j] < c[i]
            b.append(d[j])
            j += 1

    # Append any leftover elements from 'c' or 'd'.
    if i != len(c):
        b.extend(c[i:])
    if j != len(d):
        b.extend(d[j:])

    return b


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert merge_sort([2,4,3,5]) == [2,3,4,5]
    print("All tests passed!")