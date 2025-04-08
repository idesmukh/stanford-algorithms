# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement searching one array algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""


def list_search(a: list, t: int) -> bool:
    """Search list for an integer using searching one array algorithm.

    Args:
        a: List to search in.
        t: Integer to search for.

    Returns:
        bool: True, if target is found, otherwise False.
    """

    # Iterate across 'a' to search for 't'.
    for i in a:
        if i == t:
            return True

    return False


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert list_search([2, 4, 3, 5], 5) == True
    assert list_search([1, 4, 2], 8) == False
    print("All tests passed!")