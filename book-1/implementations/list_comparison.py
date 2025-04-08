# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement checking for a common element algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""


def list_comparison(a: list, b: list) -> bool:
    """Check two lists for a common integer element.

    Args:
        a: First list to search in.
        b: Second list to search in.

    Returns:
        bool: True, if common integer element is found, otherwise False.
    """

    # Iterate across 'a', and for each element in 'a', interate across 'b'.
    for i in a:
        for j in b:
            if i == j:
                return True
    
    return False


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert list_comparison([2, 4, 3, 5],[1, 9, 3]) == True
    assert list_comparison([2, 4, 3, 5],[1, 9, 1]) == False
    print("All tests passed!")