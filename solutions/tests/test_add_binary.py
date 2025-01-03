"""
Unit tests for the add_binary function.

Purpose:
    - Validate the correctness of the add_binary function.
    - Ensure the function handles edge cases, boundary cases, and invalid inputs.

Test Scenarios:
    1. Valid binary strings with various lengths and patterns.
    2. Edge cases:
        - Inputs with leading zeros.
        - Inputs consisting only of zeros.
        - Alternating binary patterns.
    3. Boundary cases:
        - Maximum allowed input length (10,000 characters).
        - Large binary strings with mixed patterns.
    4. Invalid inputs:
        - Empty strings.
        - Non-binary characters.
        - Inputs exceeding the length constraint.
        - Strings with leading or trailing spaces.

Created on 01/01/2025
@author: SiSaR-Pal
"""

import unittest

from solutions.add_binary import add_binary


class TestAddBinary(unittest.TestCase):
    """
    Unit tests for the add_binary function.
    """

    def test_basic_case(self):
        """Test addition of two small binary strings."""
        self.assertEqual(add_binary("11", "1"), "100")

    def test_different_lengths(self):
        """Test addition of binary strings with different lengths."""
        self.assertEqual(add_binary("1010", "1011"), "10101")

    def test_all_zeros(self):
        """Test addition of binary strings consisting only of zeros."""
        self.assertEqual(add_binary("0", "0"), "0")

    def test_leading_zeros(self):
        """Test addition of binary strings with leading zeros."""
        self.assertEqual(add_binary("00011", "1"), "100")

    def test_large_binary_strings(self):
        """Test addition of very large binary strings."""
        bin_num1 = "1" * 10000
        bin_num2 = "1"
        expected = "1" + "0" * 10000
        self.assertEqual(add_binary(bin_num1, bin_num2), expected)

    def test_empty_input(self):
        """Test that a ValueError is raised for empty input strings."""
        with self.assertRaises(ValueError):
            add_binary("", "1")
        with self.assertRaises(ValueError):
            add_binary("1", "")

    def test_invalid_characters(self):
        """Test that a ValueError is raised for inputs with non-binary characters."""
        with self.assertRaises(ValueError):
            add_binary("102", "1")
        with self.assertRaises(ValueError):
            add_binary("11a", "1")

    def test_whitespace_in_input(self):
        """Test that a ValueError is raised for inputs with leading or trailing spaces."""
        with self.assertRaises(ValueError):
            add_binary(" 1010 ", "101")
        with self.assertRaises(ValueError):
            add_binary("1010", " 101 ")

    def test_boundary_case_zeros(self):
        """Test addition of zeros with leading zeros."""
        self.assertEqual(add_binary("0", "00000"), "0")
        self.assertEqual(add_binary("000", "0"), "0")

    def test_alternating_pattern(self):
        """Test addition of binary strings with alternating patterns."""
        self.assertEqual(add_binary("101010", "010101"), "111111")

    def test_boundary_case_max_length_simple(self):
        """Test addition of maximum-length binary strings with simple patterns."""
        bin_num1 = "1" * 10000
        bin_num2 = "0" * 10000
        expected = "1" * 10000
        self.assertEqual(add_binary(bin_num1, bin_num2), expected)

    def test_boundary_case_max_length_mixed(self):
        """Test addition of maximum-length binary strings with mixed patterns."""
        bin_num1 = "10" * 5000
        bin_num2 = "01" * 5000
        expected = "1" * 10000
        self.assertEqual(add_binary(bin_num1, bin_num2), expected)


if __name__ == "__main__":
    unittest.main()
