# Copyright (c) 2025 Ibad Desmukh
#
# SPDX-License-Identifier: MIT
#
"""Implement the merge sort algorithm.

Reference:
Roughgarden, T. (2017). Algorithms illuminated: Part 1: The Basics.
Soundlikeyourself Publishing, LLC.
"""

import math


def merge_sort(a: list) -> list:

	# Define base case.
	# If array length is 0 or 1, it is already sorted.
	if len(a) <= 1:
		return a

if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert merge_sort([1]) == [1]
    print("All tests passed!")