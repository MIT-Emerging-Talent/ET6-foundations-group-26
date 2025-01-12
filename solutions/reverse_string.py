#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a utility function to reverse strings.

Functions:
    reverse_string(input_string: str) -> str:
        Reverses the input string and returns the reversed version.

        How it works:
- The module contains a single function, `reverse_string`, which takes a string as input and returns its reversed version.
- The function performs input validation to ensure the provided input is a string.
- If the input is valid, the string is reversed using slicing (`[::-1]`) and returned.
- If the input is not a string, the function raises a `TypeError` with an appropriate error message.

Key Features:
- Simple and efficient string reversal.
- Built-in error handling for invalid inputs.

Exceptions:
    Raises a TypeError if the input is not a string.

author : @nada-saad635

"""


def reverse_string(input_string: str) -> str:
    """
    Reverse the input string and return the reversed version.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Examples:
        >>> reverse_string("hello")
        'olleh'

        >>> reverse_string("")
        ''

        >>> reverse_string("12345")
        '54321'

    Raises:
        AssertionError: If the input is not a string.
    """
    # Ensure the input is a string
    assert isinstance(input_string, str), "Input must be a string"
    # Reverse the string using the reversed function and join the result
    reversed_string = "".join(reversed(input_string))
    return reversed_string
