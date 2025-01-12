#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the majority element in an array.

Module contents:
    - majority_element: finds the majority element in an array.

Created on 2 Jan 2025
@author: Aseel
"""


def majority_element(nums: list[int]) -> int:
    """
    Find the majority element in an array.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    It is guaranteed that such an element exists in the input.

    Parameters:
        nums (list[int]): The input list of integers.

    Returns:
        int: The majority element in the list.

    Raises:
        ValueError: If the argument is not a list of integers.
        AssertionError: If the list is empty.

    Examples:
    >>> majority_element([3, 2, 3])
    3
    >>> majority_element([2, 2, 1, 1, 1, 2, 2])
    2
    >>> majority_element([1])
    1

    Notes:
    - The input is assumed to always contain a majority element.
    """

    # Defensive check for invalid input
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of integers")

    # Check if the list is empty
    assert len(nums) > 0, "Input list must not be empty"

    # Dictionary to store the counts of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        # Return the majority element when found
        if counts[num] > len(nums) // 2:
            return num
    return None  # Should never reach this point if input is valid
