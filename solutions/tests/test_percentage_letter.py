#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the percentage_letter function.

These tests cover:

- Basic functionality
- Defensive assertions
- Boundary cases
"""

import unittest

from solutions.percentage_letter import percentage_letter


class TestPercentageLetter(unittest.TestCase):
    """Tests for the percentage_letter function."""

    def test_basic_functionality(self):
        """Test the basic calculation of percentages."""
        self.assertEqual(percentage_letter("ball", "b"), 25)

    def test_letter_not_present(self):
        """Test when the letter is not in the string."""
        self.assertEqual(percentage_letter("jjjj", "k"), 0)

    def test_letter_appears_multiple_times(self):
        """Test when the letter appears multiple times."""
        self.assertEqual(percentage_letter("accent", "c"), 33)

    def test_defensive_empty_string(self):
        """Test when the string is empty (defensive)."""
        with self.assertRaises(ValueError):
            percentage_letter("", "a")

    def test_defensive_invalid_letter(self):
        """Test when the letter is invalid (defensive)."""
        with self.assertRaises(ValueError):
            percentage_letter("foobar", "1")

    def test_boundary_string_length(self):
        """Test with boundary string length of 100 characters."""
        s = "a" * 100
        self.assertEqual(percentage_letter(s, "a"), 100)

    def test_boundary_letter_single_occurrence(self):
        """Test with boundary case where the letter occurs
        once in 100 characters."""
        s = "b" * 99 + "a"
        self.assertEqual(percentage_letter(s, "a"), 1)


if __name__ == "__main__":
    unittest.main()
