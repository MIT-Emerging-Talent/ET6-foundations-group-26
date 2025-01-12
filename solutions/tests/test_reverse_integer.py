#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Unit tests for the reverse_integer module.

This module contains a suite of tests for the reverse function, which reverses the digits
of a signed 32-bit integer, ensuring correctness and handling edge cases like overflow.
"""

import unittest
from ..reverse_integer import reverse


class TestReverseInteger(unittest.TestCase):
    """
    Test suite for the reverse function in the reverse_integer module.

    This class includes tests for typical cases, edge cases, and boundary conditions
    to ensure the function behaves as expected.
    """

    def test_positive_number(self):
        """Test reversing a positive number."""
        self.assertEqual(reverse(123), 321)

    def test_negative_number(self):
        """Test reversing a negative number."""
        self.assertEqual(reverse(-123), -321)

    def test_number_with_trailing_zero(self):
        """Test reversing a number with trailing zeros."""
        self.assertEqual(reverse(120), 21)

    def test_zero(self):
        """Test reversing zero."""
        self.assertEqual(reverse(0), 0)

    def test_positive_overflow(self):
        """Test reversing a large positive number that exceeds the 32-bit signed integer range."""
        self.assertEqual(reverse(1534236469), 0)

    def test_negative_overflow(self):
        """Test reversing a large negative number that exceeds the 32-bit signed integer range."""
        self.assertEqual(reverse(-1534236469), 0)

    def test_single_digit_positive(self):
        """Test reversing a single positive digit."""
        self.assertEqual(reverse(7), 7)

    def test_single_digit_negative(self):
        """Test reversing a single negative digit."""
        self.assertEqual(reverse(-7), -7)

    def test_large_positive_number(self):
        """Test reversing a large positive number that exceeds the 32-bit range."""
        self.assertEqual(reverse(1000000003), 0)

    def test_large_negative_number(self):
        """Test reversing a large negative number that exceeds the 32-bit range."""
        self.assertEqual(reverse(-1000000003), 0)

    def test_palindrome_number(self):
        """Test reversing a palindrome number to ensure it remains the same."""
        self.assertEqual(reverse(1221), 1221)

    def test_invalid_input(self):
        """Test that invalid input raises AssertionError."""
        with self.assertRaises(AssertionError):
            reverse(None)
        with self.assertRaises(AssertionError):
            reverse("string")
        with self.assertRaises(AssertionError):
            reverse(3.14)


if __name__ == "__main__":
    unittest.main()
