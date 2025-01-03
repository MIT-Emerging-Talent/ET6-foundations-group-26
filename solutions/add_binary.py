"""
This module provides a function to add two binary strings and return the result as a binary string.

How it works:
    - The function takes two binary strings as input.
    - Validates the inputs to ensure they:
        1. Are non-empty.
        2. Contain only '0' and '1' characters.
        3. Do not exceed the maximum length of 10,000 characters.
        4. Have no leading or trailing spaces.
    - Converts the binary strings to integers using Python's `int` function.
    - Adds the two integers and converts the result back to a binary string using `bin`.
    - Removes the '0b' prefix from the binary string and returns the result.

Constraints:
    - Input strings must consist only of '0' and '1'.
    - Input strings must not exceed 10,000 characters.
    - Input strings must not contain spaces or be empty.

Created on 01/01/2025
@author: SiSaR-Pal
"""


def add_binary(bin_num1: str, bin_num2: str) -> str:
    """
    Adds two binary strings and returns their sum as a binary string.

    Args:
        bin_num1 (str): The first binary number as a string.
        bin_num2 (str): The second binary number as a string.

    Returns:
        str: The sum of the two binary numbers as a binary string.

    Raises:
        ValueError: If inputs:
            - Are empty.
            - Contain characters other than '0' and '1'.
            - Exceed the length limit of 10,000 characters.
            - Contain leading or trailing spaces.

    Examples:
        >>> add_binary("11", "1")
        '100'
        >>> add_binary("1010", "1011")
        '10101'
        >>> add_binary("0", "000")
        '0'

    Notes:
        - Leading zeros in inputs are ignored during computation.
        - Efficiently handles binary strings up to 10,000 characters.
    """
    # Validate inputs
    if not bin_num1 or not bin_num2:
        raise ValueError("Input strings must not be empty.")
    if len(bin_num1) > 10**4 or len(bin_num2) > 10**4:
        raise ValueError("Input strings must not exceed 10,000 characters.")
    if not all(char in "01" for char in bin_num1 + bin_num2):
        raise ValueError("Input strings must contain only '0' or '1'.")
    if not bin_num1.strip() == bin_num1 or not bin_num2.strip() == bin_num2:
        raise ValueError("Input strings must not contain spaces.")

    # Perform binary addition
    return bin(int(bin_num1, 2) + int(bin_num2, 2))[2:]
