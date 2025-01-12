#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a string.

Module contents:
    - count_vowels: counts the number of vowels in a string.
Created on 30 Dec 2024
@author: Aseel
"""


def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a string.

    This function is case-insensitive and counts both uppercase and lowercase vowels.

    Parameters:
        text (str): The input string to check.

    Returns:
        int: Number of vowels in the text.

    Raises:
        ValueError: If the argument is not a string.
        AssertionError: If the string is empty.

    Examples:
    >>> count_vowels("Aseel")
    3
    >>> count_vowels("Hello World")
    3
    >>> count_vowels("Programming")
    3
    >>> count_vowels("")
    0
    >>> count_vowels("1234")
    0
    >>> count_vowels("Aeiou!")
    5
    """

    # Defensive check for invalid input
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    # Check if the string is empty
    if len(text) == 0:
        return 0

    # Define vowels
    vowels = "aeiouAEIOU"

    # Use a generator expression to count vowels efficiently
    return sum(1 for char in text if char in vowels)
