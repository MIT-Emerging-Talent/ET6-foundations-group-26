#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the convert_temperature function.
"""

import unittest
from ..convert_temperature import convert_temperature


class TestConvertTemperature(unittest.TestCase):
    """Unit tests for the convert_temperature function."""

    def test_freezing_point(self):
        """Test conversion of 0°C (freezing point of water)."""
        self.assertEqual(
            convert_temperature(0),
            {"Fahrenheit": 32.0, "Kelvin": 273.15},
            "Failed to convert freezing point",
        )

    def test_boiling_point(self):
        """Test conversion of 100°C (boiling point of water)."""
        self.assertEqual(
            convert_temperature(100),
            {"Fahrenheit": 212.0, "Kelvin": 373.15},
            "Failed to convert boiling point",
        )

    def test_absolute_zero(self):
        """Test conversion of -273.15°C (absolute zero)."""
        self.assertEqual(
            convert_temperature(-273.15),
            {"Fahrenheit": -459.67, "Kelvin": 0.0},
            "Failed to convert absolute zero",
        )

    def test_below_absolute_zero(self):
        """Test that ValueError is raised for temperatures below absolute zero."""
        with self.assertRaises(ValueError):
            convert_temperature(-300)

    def test_decimal_value(self):
        """Test conversion of a temperature with decimal places."""
        self.assertEqual(
            convert_temperature(25.6),
            {"Fahrenheit": 78.08, "Kelvin": 298.75},
            "Failed to convert decimal temperature",
        )

    def test_negative_value(self):
        """Test conversion of a negative temperature."""
        self.assertEqual(
            convert_temperature(-100),
            {"Fahrenheit": -148.0, "Kelvin": 173.15},
            "Failed to convert negative temperature",
        )


if __name__ == "__main__":
    unittest.main()
