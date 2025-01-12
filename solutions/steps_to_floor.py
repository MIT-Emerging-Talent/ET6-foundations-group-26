#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Building Steps Calculator

This module provides functionality to calculate
 the number of steps required to reach a specific floor
   in a building. It includes a core function
     for the calculation and a wrapper function for handling user input.
"""


def steps_to_floor_core(target_floor: int) -> int:
    """
    Core function to calculate the number of steps required to reach a given floor in a building,
    assuming it takes 10 steps to move between consecutive floors.

    Parameters:
      target_floor: int, the floor number to reach (positive, negative, or zero).

    Returns:
      int: the total number of steps required.

    Raises:
      AssertionError: If the target_floor is not an integer.

    Examples:
    >>> steps_to_floor_core(0)
    0
    >>> steps_to_floor_core(1)
    10
    >>> steps_to_floor_core(5)
    50
    >>> steps_to_floor_core(-3)
    30
    """
    # Defensive assertion to ensure valid input
    assert isinstance(target_floor, int), "Target floor must be an integer"

    # Calculate steps based on the absolute floor value
    return abs(target_floor) * 10


def steps_to_floor():
    """
    Wrapper function to handle user input for steps_to_floor_core.
    """
    try:
        target_floor = int(input("Enter the floor number you want to reach: "))
        steps = steps_to_floor_core(target_floor)
        if target_floor < 0:
            return f"You are going down. Steps required: {steps}"
        elif target_floor > 0:
            return f"You are going up. Steps required: {steps}"
        else:
            return f"You are staying on the same floor. Steps required: {steps}"
    except ValueError:
        return "Invalid input. Please enter an integer."
    except AssertionError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Run tests on the core function
    # Uncomment the following line for interactive user input
    steps_to_floor()
