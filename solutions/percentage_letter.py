#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides function to calculate the percentage of characters
in a string that match a specified letter,
rounded down to the nearest whole percent.

The function ensures:
- The string is non-empty.
- The letter is a single lowercase English letter.

    Args:
        text (str): The input string (must have a length between 1 and 100).
        letter (str): A single lowercase English letter to count in the string.

    Returns:
        int: The percentage (0-100) of occurrences of letter in s,
        rounded down to the nearest whole number.

    Raises:
        ValueError: If the string is empty or the letter
        is not a single lowercase English character.

    Examples:
        >>> percentage_letter("hello", "l")
        40
        >>> percentage_letter("world", "w")
        20
        >>> percentage_letter("calculations", "z")
        0
"""


def percentage_letter(text: str, letter: str) -> int:
    # Defensive assertions
    if not (1 <= len(text) <= 100):
        raise ValueError("The string must have a length between 1 and 100.")
    if not (len(letter) == 1 and letter.islower() and letter.isalpha()):
        raise ValueError("The letter must be a single lowercase English character.")

    # Count occurrences of the letter in the string
    count_letters = text.count(letter)

    # Calculate the percentage rounded down
    return int((count_letters / len(text)) * 100)
