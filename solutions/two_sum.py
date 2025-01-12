#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a function to solve the two-sum problem.
"""

from typing import List


class NoTwoSumSolutionError(Exception):
    """Raised when no two numbers in the list sum to the target."""

    pass


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns indices of the two numbers in the array that add up to the target.

    Args:
        nums (List[int]): A list of integers. Length must be >= 2.
        target (int): The target sum for the two integers.

    Returns:
        List[int]: A list containing two indices of
        numbers that add up to the target.

    Raises:
        ValueError: If no two numbers in the list sum to the target.

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]
    """
    # Validate input list length
    if len(nums) < 2:
        raise ValueError("The input list must contain at least two integers.")

    # Validate input types
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All elements in the input list must be integers.")

    seen_values = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_values:
            return [seen_values[complement], i]
        seen_values[num] = i

    raise ValueError("No two sum solution exists.")
