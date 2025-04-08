# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement searching two arrays algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""


def two_list_search(a: list, b: list, t: int) -> bool:
    """Search two lists for an integer using searching two arrays algorithm.

    Args:
        a: First list to search in.
        b: Second list to search in.
        t: Integer to search for.

    Returns:
        bool: True, if target is found, otherwise False.
    """
    
    # Iterate across 'a' to search for 't'.
    for i in a:
        if i == t:
            return True
    
    # Iterate across 'b' to search for 't'.
    for i in b:
        if i == t:
            return True
    
    return False


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert two_list_search([2, 4, 3, 5],[1, 9, 8, 5], 5) == True
    print("All tests passed!")