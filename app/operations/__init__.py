"""
This __init__.py file is now being updated for assignment 3 to work with the new class definitions.

For brevity's sake, I haven't repeated the descriptions of each opertation here. They can be found in test_operations.py, within the tests folder.
"""
class operations:
    @staticmethod
    def addition(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:

        """
    There's an important check here: before we divide, we need to make sure that 'b' is not zero.
    
    Why? Because dividing by zero doesn't work. If we try to divide by zero, we get a big error!
    
    So, if 'b' is zero, we raise a 'ZeroDivisionError', which is a way of telling the program, "Stop! You can't do this."
    Example: if we call division(10.0, 2.0), it will return 5.0.
    But if we call division(10.0, 0.0), it will raise a ZeroDivisionError and say "Cannot."
        """
        if b == 0:
        # This part checks if 'b' is zero. If it is, we raise an error and stop the function.
            raise ZeroDivisionError("Cannot divide by zero")  # This sends an error message when someone tries to divide by zero.
        return a / b  # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the result.