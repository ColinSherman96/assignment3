"""These are the unit tests for the operations module. While it may not be necessary for me to write this description, we are practicing coding conventions - so I figured it would be a good habit to get in the practice of describing what each section of my project does. Here, we introduce parameterized tests - allowing for the same testing as with Assignment 2, but with less duplicate code."""

import pytest
from typing import Union # Looking at the template, seems like this is used for the type hinting mentioned in the modules
from app.operations import operations

Number = Union[int, float] # This is a type hinting alias, allowing us to use 'Number' instead of writing 'Union[int, float]' every time we want to specify that a variable can be either an int or a float.

"""
Hello Prof. Williams, Arash, or whoever may be reading this! Just wanted to say that I am enjoying the course and hope you are doing well. Here's a coding duck to brighten your day a bit!

⡀⣠⣴⣶⣶⣿⣿⣷⣶⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢶⣾⣿⡿⠿⠉⠉⠉⠉⠹⠿⣿⣿⣿⣆⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⣙⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠙⣿⣿⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⡇⠀⣀⣀⠀⠀⠀⠀⣰⣦⣤⣠⣤⣤⣤⣄⡘⣿⣷⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⡇⠘⣿⣿⠇⠀⠀⣴⡿⢁⣉⣭⣥⣤⣼⣿⠇⢹⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢺⣿⣧⠀⠀⠀⢀⣴⡿⢏⣴⣿⠟⢉⣩⣽⠟⠁⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⣿⡆⠀⢀⣾⣏⣴⡿⣛⣥⣶⠿⠋⠁⠀⠀⠀⠀⢸⣿⣿⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣷⠀⣾⣿⣿⡿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣶⣄⡙⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⡍⠛⠿⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⠀⠀⠀⠀⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣮⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⣿⣿⠀⠀⠀⠀⠈⢿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠄⠀⠀⠀⠀⠀⠀⠀
⢐⣿⣿⣿⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠈⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⠀
⢸⣿⡄⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⠀⠀⠀⠀⠀⠀
⠹⣿⣧⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡗⡀⠀⠀⠀⠀
⠀⢻⣿⣆⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡧⡇⠀⠀⠀⠀
⠀⢸⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣇⠃⠀⠀⠀⠀
⠀⠘⣿⣧⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⠹⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣧⣶⣧⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠈⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣾⣿⣿⡿⡟⣿⣿⣶⣀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠈⠈⢟⢿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣟⣟⡻⢏⣳⣽⣷⢎⡽⢻⣿⣷⣿⡷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⠿⣿⣮⡷⣋⢾⡻⣝⣮⣼⣿⣿⡿⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣯⣿⣿⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠉⠻⠿⡿⠾⠿⠿⠿⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣿⣇⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣏⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# ---------------------------
# Unit tests for 'addition'
# ---------------------------

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, 6),          # Test with two integers
    (1.5, 2.5, 4.0),    # Test with two positive floats
    (-1, -2, -3),       # Test with negative integers
    (-1, 1, 0),        # Test with a negative and a positive integer
    (-2.5, 4.5, 2.0),    # Test with a negative and a positive float
    (0, 0, 0),          # Test with zeros
    (1, -1, 0),         # Test with a positive and a negative integer
    ], 
    ids=[
        "add_two_integers",
        "add_two_positive_floats",
        "add_two_negative_integers",
        "add_negative_and_positive_integer",
        "add_negative_and_positive_float",
        "add_zeros",
        "add_positive_and_negative_integer"
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
    """
    Test the addition method of the Operations class with various inputs.
    
        Parameters:
            a (Number): The first number to add.
            b (Number): The second number to add.
            expected (Number): The expected result of the addition.
                        
        Returns:
            None: This function does not return anything, it will raise an assertion error if the test fails.

        Steps:
            1. Call the addition method with the provided inputs.
            2. Assert that the result matches the expected value. 
        
        Example:
            Given a = 2, b = 4, and expected = 6, when the addition method is called, it should return 6. If it returns anything other than
            6, the test will fail and an assertion error will be raised with a message indicating the expected and actual results.
    """
    # Call the addition method
    result = operations.addition(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected addition({a}, {b}) to be {expected} but got {result}"

# ---------------------------
# Unit tests for 'subtraction'
# ---------------------------

@pytest.mark.parametrize("a, b, expected", [
    (5, 1, 4),          # Test with two integers
    (5.5, 2.5, 3.0),    # Test with two floats
    (-1, -2, 1),       # Test with negative integers
    (-1, 1, -2),       # Test with a negative and a positive integer
    (-2.5, 4.5, -7.0), # Test with a negative and a positive float
    (0, 0, 0),         # Test with zeros
    (1, -1, 2),        # Test with a positive and a negative integer
    ],
    ids=[
        "subtract_two_integers",
        "subtract_two_floats",
        "subtract_two_negative_integers",
        "subtract_negative_and_positive_integer",
        "subtract_negative_and_positive_float",
        "subtract_zeros",
        "subtract_positive_and_negative_integer"
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """
    Test the subtraction method of the Operations class with various inputs.
    
        Parameters:
            a (Number): The first number to subtract from.
            b (Number): The second number to subtract.
            expected (Number): The expected result of the subtraction.
                        
        Returns:
            None: This function does not return anything, it will raise an assertion error if the test fails.

        Steps:
            1. Call the subtraction method with the provided inputs.
            2. Assert that the result matches the expected value. 
        
        Example:
            Given a = 5, b = 3, and expected = 2, when the subtraction method is called, it should return 2. If it returns anything other than
            2, the test will fail and an assertion error will be raised with a message indicating the expected and actual results.
    """
    # Call the subtraction method
    result = operations.subtraction(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected} but got {result}"

# ---------------------------
# Unit tests for 'multiplication'
# ---------------------------

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),         # Test with two integers
    (2.5, 4.0, 10.0),   # Test with two floats
    (-1, -2, 2),       # Test with negative integers
    (-1, 1, -1),       # Test with a negative and a positive
    (-2.5, 4.5, -11.25), # Test with a negative and a positive float
    (0, 5, 0),         # Test with zero and a positive integer
    (1, -1, -1),       # Test with a positive and a negative integer
    ],
    ids=[
        "multiply_two_integers",
        "multiply_two_floats",
        "multiply_two_negative_integers",
        "multiply_negative_and_positive",
        "multiply_negative_and_positive_float",
        "multiply_zero_and_positive_integer",
        "multiply_positive_and_negative_integer"
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """
    Test the multiplication method of the Operations class with various inputs.
    
        Parameters:
            a (Number): The first number to multiply.
            b (Number): The second number to multiply.
            expected (Number): The expected result of the multiplication.
                        
        Returns:
            None: This function does not return anything, it will raise an assertion error if the test fails.

        Steps:
            1. Call the multiplication method with the provided inputs.
            2. Assert that the result matches the expected value. 
        
        Example:
            Given a = 3, b = 4, and expected = 12, when the multiplication method is called, it should return 12. If it returns anything other than
            12, the test will fail and an assertion error will be raised with a message indicating the expected and actual results.
    """
    # Call the multiplication method
    result = operations.multiplication(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected} but got {result}"

# ---------------------------
# Unit tests for 'division'
# ---------------------------

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),         # Test with two integers
    (5.0, 2.0, 2.5),    # Test
    (-10, -2, 5),      # Test with negative integers
    (-10, 2, -5),      # Test with a negative and a positive integer
    (-10.0, 2.0, -5.0), # Test with a negative and a positive float
    (0, 5, 0),         # Test with zero and a positive integer
    (1, -1, -1),       # Test with a positive and a negative integer
    ],
    ids=[
        "divide_two_integers",
        "divide_two_floats",
        "divide_two_negative_integers",
        "divide_negative_and_positive_integer",
        "divide_negative_and_positive_float",
        "divide_zero_and_positive_integer",
        "divide_positive_and_negative_integer"
    ]
)
def test_division(a: Number, b: Number, expected: Number) -> None:
    """
    Test the division method of the Operations class with various inputs.
    
        Parameters:
            a (Number): The numerator.
            b (Number): The denominator.
            expected (Number): The expected result of the division.
                        
        Returns:
            None: This function does not return anything, it will raise an assertion error if the test fails.

        Steps:
            1. Call the division method with the provided inputs.
            2. Assert that the result matches the expected value. 
        
        Example:
            Given a = 10, b = 2, and expected = 5, when the division method is called, it should return 5. If it returns anything other than
            5, the test will fail and an assertion error will be raised with a message indicating the expected and actual results.
    """
    # Call the division method
    result = operations.division(a, b)

    # Assert that the result matches the expected value
    assert result == expected, f"Expected division({a}, {b}) to be {expected} but got {result}"

# ---------------------------
# Unit tests for dividing by zero
# ---------------------------

@pytest.mark.parametrize("a, b", [
    (10, 0),        # Test with an integer numerator and zero denominator
    (5.0, 0.0),     # Test with a float numerator and zero denominator
    (-10, 0),       # Test with a negative integer numerator and zero denominator
    (-10.0, 0.0),    # Test with a negative float numerator and zero denominator
    (0, 0),         # Test with zero numerator and zero denominator
    ],
    ids=[
        "divide_integer_by_zero",
        "divide_float_by_zero",
        "divide_negative_integer_by_zero",
        "divide_negative_float_by_zero",
        "divide_zero_by_zero"
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    """
    Test the division method of the Operations class when dividing by zero.
    
        Parameters:
            a (Number): The numerator.
            b (Number): The denominator (which is zero in this case).
                        
        Returns:
            None: This function does not return anything, it will raise an assertion error if the test fails.

        Steps:
            1. Call the division method with the provided inputs.
            2. Assert that a ZeroDivisionError is raised when attempting to divide by zero. 
        
        Example:
            Given a = 10 and b = 0, when the division method is called, it should raise a ValueError. If it does not raise this error, the test will fail and an assertion error will be raised with a message indicating that a ZeroDivisionError was expected but not raised.
    """
    # Assert that a ZeroDivisionError is raised when attempting to divide by zero
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero") as exc_info:
        operations.division(a, b)
    
    # Assert that the exception message is correct
    assert "Cannot divide by zero" in str(exc_info.value), \
        f"Expected ZeroDivisionError with message 'Cannot divide by zero' but got '{(exc_info.value)}'"  
    
