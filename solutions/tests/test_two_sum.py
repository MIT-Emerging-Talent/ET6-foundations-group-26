#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the two_sum function.
"""

import unittest

from solutions.two_sum import two_sum

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


class TestTwoSum(unittest.TestCase):
    """
    Unit tests for the two_sum function.
    """

    def test_valid_input(self):
        """
        Tests valid inputs where two numbers sum up to the target.
        """
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        """
        Tests the function with negative numbers in the list.
        """
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_large_numbers(self):
        """
        Tests the function with large numbers in the list.
        """
        self.assertEqual(two_sum([1000000, 500000, -1500000], -500000), [0, 2])

    def test_value_error(self):
        """
        Tests that a ValueError is raised when no solution exists.
        """
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 7)


def test_empty_or_single_element_list(self):
    """
    Test the two_sum function with edge cases:
    - An empty list
    - A single-element list

    Ensures that the function raises a ValueError when it is not
    possible to find two numbers that add up to the target.
    """
    with self.assertRaises(ValueError):
        two_sum([], 9)
    with self.assertRaises(ValueError):
        two_sum([5], 5)


if __name__ == "__main__":
    unittest.main()
