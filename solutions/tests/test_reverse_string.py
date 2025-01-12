#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the reverse_string function.

This module contains several test cases to verify the functionality of the reverse_string function.
It checks the expected behavior for a variety of inputs including:
- A normal string.
- An empty string.
- A string with special characters.
- A string with spaces.
"""

import unittest
from ..reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    """
    Test cases for the reverse_string function.
    """

    def test_regular_string(self):
        """Test reversing a regular string."""
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_palindrome(self):
        """Test reversing a palindrome (same forward and backward)."""
        self.assertEqual(reverse_string("madam"), "madam")

    def test_numbers_in_string(self):
        """Test reversing a string containing numbers."""
        self.assertEqual(reverse_string("12345"), "54321")

    def test_special_characters(self):
        """Test reversing a string with special characters."""
        self.assertEqual(reverse_string("!@#$"), "$#@!")

    def test_long_string(self):
        """Test reversing an extremely long string."""
        long_string = "a" * 10000
        self.assertEqual(reverse_string(long_string), long_string[::-1])

    def test_integer_input(self):
        """Test that an integer input raises an AssertionError."""
        with self.assertRaises(AssertionError):
            reverse_string(12345)  # Non-string input: integer

    def test_none_input(self):
        """Test that a None input raises an AssertionError."""
        with self.assertRaises(AssertionError):
            reverse_string(None)  # Non-string input: NoneType

    def test_list_input(self):
        """Test that a list input raises an AssertionError."""
        with self.assertRaises(AssertionError):
            reverse_string(["a", "b", "c"])  # Non-string input: list


if __name__ == "__main__":
    unittest.main()
