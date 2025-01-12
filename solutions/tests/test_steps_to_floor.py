#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the steps_to_floor_core function, which calculates the number
of steps required to reach a specified floor.
"""

import unittest
from ..steps_to_floor import steps_to_floor_core


class TestStepsToFloor(unittest.TestCase):
    """
    Unit tests for the steps_to_floor_core function, which calculates the number
    of steps required to reach a specified floor.
    """

    def test_zero_floor(self):
        """Test that 0 steps are required to reach the ground floor (floor 0)."""
        self.assertEqual(steps_to_floor_core(0), 0)

    def test_positive_floor(self):
        """Test that the correct number of steps is returned for a positive floor number."""
        self.assertEqual(steps_to_floor_core(1), 10)

    def test_negative_floor(self):
        """Test that the correct number of steps is returned for a negative floor number."""
        self.assertEqual(steps_to_floor_core(-3), 30)

    def test_invalid_non_integer_input(self):
        """
        Test that the function raises an AssertionError for non-integer input.
        """
        with self.assertRaises(AssertionError):
            steps_to_floor_core("a")  # Non-integer input

    def test_invalid_float_input(self):
        """
        Test that the function raises an AssertionError for float input.
        """
        with self.assertRaises(AssertionError):
            steps_to_floor_core(5.5)  # Float input


if __name__ == "__main__":
    unittest.main()
