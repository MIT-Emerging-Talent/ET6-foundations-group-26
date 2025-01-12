#!/usr/bin/env python3
# -- coding: utf-8 --
"""
A module for explaining FizzBuzz functionality.

This module includes the function fizzbuzz(n) that returns:
- 'Fizz' for numbers divisible by 3.
- 'Buzz' for numbers divisible by 5.
- 'FizzBuzz' for numbers divisible by both 3 and 5.
- The number itself as a string for all other cases.

author : @nada-saad635

"""


def fizz_buzz(number: int) -> str:
    """
        Returns 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
        'FizzBuzz' for multiples of both 3 and 5, and the number itself for others.

        parameters:
            number (int): The number to evaluate.

        Returns:
            str: 'Fizz', 'Buzz', 'FizzBuzz', or the string representation of the number.
    >>> fizz_buzz(15)
    'FizzBuzz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(7)
    '7'

    """
    assert isinstance(number, int), "Input must be an integer"
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
