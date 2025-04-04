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

    # Define base case.
    # If list length is 0 or 1, it is already sorted.
    if len(a) <= 1:
        return a

    # Define recursive case.
    # Divide the list into two halves.
    middle_index = len(a) // 2
    a_left = a[:middle_index]
    a_right = a[middle_index:]

    sorted_left = merge_sort(a_left)
    sorted_right = merge_sort(a_right)

    return merge(sorted_left, sorted_right)


def merge(c: list, d: list) -> list:
    # Initialize output list.
    b = []

    # Initialise pointers for c and d.
    i = 0
    j = 0

    while i < len(c) and j < len(d):
        if c[i] < d[j]:
            b.append(c[i]) # Populate output list.
            i += 1 # Increment i.
        else: # d[j] < c[i]
            b.append(d[j])
            j += 1

    # Append any leftover elements from c or d.
    if i != len(c):
        b.extend(c[i:])
    if j != len(d):
        b.extend(d[j:])

    return b


if __name__ == "__main__":
    # Verify the algorithm with a simple test case.
    assert merge_sort([2,4,3,5]) == [2,3,4,5]
    print("All tests passed!")