#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the majority_element module.

This module contains a suite of tests for the majority_element function,
which finds the majority element in a given list of integers. The majority
element is the one that appears more than ⌊n / 2⌋ times, and it is assumed
to always exist in the input.

Examples:
    majority_element([3, 2, 3]) -> 3
    majority_element([2, 2, 1, 1, 1, 2, 2]) -> 2

Created on 2 Jan 2025
@author: Aseel
"""

import unittest
from solutions.majority_element import majority_element


class TestMajorityElement(unittest.TestCase):
    """
    Test case for the majority_element function.
    """

    # Standard tests to validate functionality
    def test_majority_element_basic_case(self):
        """Test that majority_element works for a simple case."""
        self.assertEqual(majority_element([3, 2, 3]), 3)

    def test_majority_element_unique_majority(self):
        """Test that majority_element identifies a unique majority element."""
        self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_majority_element_single_element(self):
        """Test that majority_element works for a single-element list."""
        self.assertEqual(majority_element([1]), 1)

    def test_majority_element_all_same(self):
        """Test that majority_element works when all elements are the same."""
        self.assertEqual(majority_element([5, 5, 5, 5]), 5)

    def test_majority_element_large_input(self):
        """Test that majority_element works for a large input."""
        large_input = [1] * 50000 + [2] * 49999
        self.assertEqual(majority_element(large_input), 1)

    # Defensive tests for invalid input
    def test_majority_element_empty_list(self):
        """Test that majority_element raises an AssertionError for an empty list."""
        with self.assertRaises(AssertionError):
            majority_element([])

    def test_majority_element_invalid_input(self):
        """Test that majority_element raises a ValueError for invalid input."""
        with self.assertRaises(ValueError):
            majority_element("not a list")  # Passing a string instead of a list

    def test_majority_element_non_integer_elements(self):
        """Test that majority_element raises a ValueError for non-integer elements."""
        with self.assertRaises(ValueError):
            majority_element([1, 2, "3", 4])  # List contains a string

    # Edge cases
    def test_majority_element_majority_at_start(self):
        """Test when the majority element appears at the start of the list."""
        self.assertEqual(majority_element([4, 4, 4, 1, 2, 3, 4, 4]), 4)

    def test_majority_element_majority_at_end(self):
        """Test when the majority element appears at the end of the list."""
        self.assertEqual(majority_element([1, 2, 3, 4, 4, 4, 4]), 4)

    def test_majority_element_alternating_majority(self):
        """Test when the majority element alternates with other elements."""
        self.assertEqual(majority_element([1, 2, 1, 2, 1, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
