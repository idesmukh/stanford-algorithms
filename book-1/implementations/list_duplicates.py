# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement checking for duplicates algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""


def list_duplicates(a: list) -> bool:
    """Check for duplicates in a list.

    Args:
        a: List of n integers.
    
    Returns:
        bool: True if 'a' contains an integer more than once, otherwise False.
    """

    # Determine length of 'a'.
    n = len(a)

    # Iterate from first element to second last.
    for i in range(n):
        # Iterate from one element after current element, upto last element.
        for j in range(i + 1, n):
            if a[i] == a[j]:
                return True
    
    return False


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert list_duplicates([2, 1, 1, 8]) == True
    assert list_duplicates([2, 1, 4, 8]) == False
    print("All tests passed!")