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
