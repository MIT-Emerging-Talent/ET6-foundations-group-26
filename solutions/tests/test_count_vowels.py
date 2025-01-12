#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the count_vowels module.

This module contains a suite of tests for the count_vowels function, which counts
the number of vowels in a given string. The function handles both uppercase
and lowercase vowels and ensures correct results for edge cases, such as
empty strings, strings with no vowels, and strings with special characters
or whitespace.

Examples:
    count_vowels("hello") -> 2
    count_vowels("HELLO") -> 2
    count_vowels(" A e i o u ") -> 5

Created on 30 Dec 2024
@author: Aseel
"""

import unittest
from solutions.count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """
    Test case for the count_vowels function.
    """

    # Standard tests to validate the functionality
    def test_count_vowels_basic_case(self):
        """Test that count_vowels works for a simple case."""
        self.assertEqual(count_vowels("Aseel"), 3)

    def test_count_vowels_empty_string(self):
        """Test that count_vowels returns 0 for an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """Test that count_vowels returns 0 when there are no vowels."""
        self.assertEqual(count_vowels("1234"), 0)

    def test_count_vowels_special_characters(self):
        """Test that count_vowels handles special characters correctly."""
        self.assertEqual(count_vowels("Aeiou!"), 5)

    def test_count_vowels_case_insensitive(self):
        """Test that count_vowels is case-insensitive."""
        self.assertEqual(count_vowels("aEiOu"), 5)

    def test_count_vowels_only_consonants(self):
        """Test that count_vowels returns 0 when there are only consonants."""
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_count_vowels_large_input(self):
        """Test that count_vowels works for very large strings."""
        large_input = "a" * 1000000  # 1 million vowels
        self.assertEqual(count_vowels(large_input), 1000000)

    def test_count_vowels_with_numbers_and_symbols(self):
        """Test that count_vowels correctly counts vowels with numbers and symbols."""
        self.assertEqual(count_vowels("1234!@#$%^&*()"), 0)

    def test_count_vowels_mixed_case_and_symbols(self):
        """Test that count_vowels correctly handles mixed case with symbols."""
        self.assertEqual(count_vowels("Aeiou123!"), 5)

    def test_vowel_count_with_whitespace(self):
        """Test count_vowels function with input containing whitespace."""
        result = count_vowels(" A e i o u ")
        self.assertEqual(result, 5)  # Expect 5 vowels

    # Defensive test to validate error handling for invalid input
    def test_count_vowels_invalid_input(self):
        """Test that count_vowels raises a ValueError for invalid input."""
        with self.assertRaises(ValueError):
            count_vowels(1234)  # Passing an integer instead of a string


if __name__ == "__main__":
    unittest.main()
