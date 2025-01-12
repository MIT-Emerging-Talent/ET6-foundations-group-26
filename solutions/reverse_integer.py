#!/usr/bin/env python3
# -- coding: utf-8 --
class ReverseIntegerError(Exception):
    """Custom exception for reverse integer errors."""

    pass


def reverse(input_number: int) -> int:
    """
    Reverses the digits of a signed 32-bit integer.

    Parameters:
    input_number (int): The integer to reverse.

    Returns:
    int: The reversed integer if it falls within the signed 32-bit range [-2^31, 2^31 - 1].
         Returns 0 if the reversed integer overflows.

    Raises:
    AssertionError: If the argument is not an integer.
    MemoryError: If the operation exceeds memory limits for large inputs.
    ReverseIntegerError: If the input is outside a specified range.

    Examples:
    >>> reverse(123)
    321
    >>> reverse(-123)
    -321
    >>> reverse(120)
    21
    >>> reverse(0)
    0
    """
    # Assert that the input is an integer
    assert isinstance(input_number, int), "Input must be an integer"

    # Define the range for signed 32-bit integers
    INT_MIN, INT_MAX = -(2**31), 2**31 - 1

    # Raise custom exception if input is out of bounds
    if input_number < INT_MIN or input_number > INT_MAX:
        raise ReverseIntegerError("Input is outside the 32-bit signed integer range")

    # Simulate potential memory errors for extremely large inputs (unlikely in practical scenarios)
    try:
        # Determine if the number is negative
        negative = input_number < 0

        # Work with the absolute value of input_number
        input_number = abs(input_number)

        # Reverse the digits using string manipulation
        reversed_x = int(str(input_number)[::-1])

        # Restore the sign if the number was negative
        if negative:
            reversed_x = -reversed_x

        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x

    except MemoryError:
        raise MemoryError("Operation exceeded memory limits for large inputs")
