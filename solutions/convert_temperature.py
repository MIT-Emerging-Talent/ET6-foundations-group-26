#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides functionality to convert temperatures from Celsius
to Fahrenheit and Kelvin.
functions:
    - convert_temperature(celsius: float) -> dict[str, float]
"""


def convert_temperature(celsius: float) -> dict[str, float]:
    """
    Convert temperature from Celsius to Fahrenheit and Kelvin.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        dict: A dictionary containing the temperature in Fahrenheit and Kelvin.

    Raises:
        ValueError: If the input is not a valid number or is below absolute zero.

    Examples:
        >>> convert_temperature(0)
        {'Fahrenheit': 32.0, 'Kelvin': 273.15}
        >>> convert_temperature(-273.15)
        {'Fahrenheit': -459.67, 'Kelvin': 0.0}
        >>> convert_temperature(100)
        {'Fahrenheit': 212.0, 'Kelvin': 373.15}
        >>> convert_temperature(-300)  # Below absolute zero
        Traceback (most recent call last):
        ValueError: Temperature cannot be below absolute zero (-273.15°C).
    """
    # Check if the input is a valid number (int or float)
    if not isinstance(celsius, (int, float)):
        raise TypeError("The input temperature must be a number.")
    # Ensure the input temperature is not below absolute zero (-273.15°C)
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    # Convert Celsius to Fahrenheit and Kelvin
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15

    return {"Fahrenheit": round(fahrenheit, 2), "Kelvin": round(kelvin, 2)}


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Run doctests
