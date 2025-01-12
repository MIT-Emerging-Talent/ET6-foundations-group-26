#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from solutions.fizz_buzz import fizz_buzz

"""
Write a program that prints numbers from 1 to 100. However:
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For numbers that are multiples of both 3 and 5, print "FizzBuzz".
"""


class TestFizzBuzz(unittest.TestCase):
    """Unit tests for the fizz_buzz function."""

    def test_fizz(self):
        """Test that fizz_buzz returns 'Fizz' for multiples of 3."""
        self.assertEqual(fizz_buzz(3), "Fizz")  # Multiple of 3

    def test_buzz(self):
        """Test that fizz_buzz returns 'Buzz' for multiples of 5."""
        self.assertEqual(fizz_buzz(5), "Buzz")  # Multiple of 5

    def test_fizz_buzz(self):
        """Test that fizz_buzz returns 'FizzBuzz' for multiples of both 3 and 5."""
        self.assertEqual(fizz_buzz(15), "FizzBuzz")  # Multiple of both 3 and 5

    def test_number(self):
        """returns the number as a string if it's neither a multiple of 3 nor 5."""
        self.assertEqual(fizz_buzz(1), "1")  # Neither multiple of 3 nor 5

    def test_large_number(self):
        """Test behavior with a very large number."""
        self.assertEqual(fizz_buzz(300000), "FizzBuzz")  # Divisible by 3 and 5

    def test_negative_fizz(self):
        """Test behavior with a negative multiple of 3."""
        self.assertEqual(fizz_buzz(-9), "Fizz")  # Negative multiple of 3

    def test_zero(self):
        """Test behavior with zero."""
        self.assertEqual(fizz_buzz(0), "FizzBuzz")  # Divisible by any number

    def test_none_input(self):
        """Test that fizz_buzz raises an AssertionError when input is None."""
        with self.assertRaises(AssertionError):
            fizz_buzz(None)


if __name__ == "__main__":
    unittest.main()
